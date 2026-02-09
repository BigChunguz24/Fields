# Build a clean virtualenv
FROM docker-hub-repo.amana.vpn/python:3.10-slim AS build
ENV PATH="/venv/bin:$PATH"
RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --upgrade gunicorn && \
    /venv/bin/pip install --upgrade wheel


# Build the virtualenv when requirements.txt changes
FROM build AS build-venv
ENV PATH="/venv/bin:$PATH"
COPY ./requirements.txt /requirements.txt

# Install GCC for XGBoost
RUN apt update && apt -y install gcc && rm -rf /var/lib/apt/lists/*

RUN /venv/bin/pip install --trusted-host maven.amana.vpn --disable-pip-version-check -r /requirements.txt

# Copy and run the script
FROM docker-hub-repo.amana.vpn/python:3.10-slim as run
ENV PATH="/venv/bin:$PATH"
COPY --from=build-venv /venv /venv

RUN addgroup --gid 12345 python-lab && adduser python-lab --ingroup python-lab --uid 12345 --disabled-password --gecos ''

# Install punkt tokeniser for NLTK
RUN python -c "import nltk;nltk.download('punkt', download_dir='/usr/share/nltk_data')"

# Install LibGomp for XGBoost
RUN apt update && apt -y install libgomp1 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /python-lab
COPY resources /python-lab/resources
COPY scripts /python-lab/scripts
COPY info.properties /python-lab/
COPY movequant /python-lab/movequant
RUN chown -R python-lab:python-lab /python-lab
ENV PYTHONPATH="/python-lab:$PYTHONPATH"

# Add current commit information and date/time to info.properties
ARG VERSION
RUN echo "writing information to info.properties"
RUN sed -i "s/\(^build.version=\).*$/\1${VERSION}/" /python-lab/info.properties
RUN sed -i "s/\(^build.time=\).*$/\1$(date +"%Y-%m-%d %T %Z")/" /python-lab/info.properties

USER 12345
EXPOSE 5000
WORKDIR /python-lab
ENV PYTHONPATH="/python-lab:$PYTHONPATH"
CMD /venv/bin/gunicorn --workers $WORKERS \
  --threads $THREADS \
  --bind 0.0.0.0:5000 \
  --reload \
  --log-level $LOG_LEVEL \
  --timeout $TIMEOUT \
  movequant.wsgi:app
