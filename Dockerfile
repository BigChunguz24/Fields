# -------- Build a clean virtualenv --------
FROM python:3.10-slim AS build

ENV VENV_PATH=/venv
ENV PATH="$VENV_PATH/bin:$PATH"

RUN python -m venv $VENV_PATH && \
    pip install --upgrade pip wheel gunicorn

# Build the virtualenv when requirements.txt changes
FROM build AS build-venv

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy and run the script
FROM python:3.10-slim AS run

ENV PATH="/venv/bin:$PATH"

COPY --from=build-venv /venv /venv

# Non-root user
RUN addgroup --gid 12345 project_fields && \
    adduser --uid 12345 --gid 12345 --disabled-password --gecos "" project_fields

# Add current commit information and date/time to info.properties // Metadata injection //
ARG VERSION
RUN mkdir -p /project_fields && \
    touch /project_fields/info.properties && \
    # Set build.version
    grep -q '^build.version=' /project_fields/info.properties \
        && sed -i "s/^build.version=.*/build.version=${VERSION}/" /project_fields/info.properties \
        || echo "build.version=${VERSION}" >> /project_fields/info.properties && \
    # Set build.time
    grep -q '^build.time=' /project_fields/info.properties \
        && sed -i "s/^build.time=.*/build.time=$(date +"%Y-%m-%d %T %Z")/" /project_fields/info.properties \
        || echo "build.time=$(date +"%Y-%m-%d %T %Z")" >> /project_fields/info.properties


USER 12345
WORKDIR /project_fields
ENV PYTHONPATH="/project_fields:$PYTHONPATH"
EXPOSE 5000

CMD /venv/bin/gunicorn --workers ${WORKERS:-2} \
  --threads ${THREADS:-2} \
  --bind 0.0.0.0:5000 \
  --reload \
  --log-level ${LOG_LEVEL:-info} \
  --timeout ${TIMEOUT:-30} \
  movequant.wsgi:app