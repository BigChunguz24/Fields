### -------- Build a clean virtualenv -------- ###
# Starts a build with Python 3.13 and defines an environment variable for the venv location within the container.
# Then it adds the venv's executable to PATH, so commands such as "python" and "pip" use the venv by default.
# Finally, it creates the venv in the container and installs or upgrades the "pip" and "wheel" packages, if successful.
FROM python:3.13-slim AS build

ENV VENV_PATH=/venv
ENV PATH="$VENV_PATH/bin:$PATH"

RUN python -m venv "$VENV_PATH" && pip install --upgrade pip wheel

### -------- Build the virtualenv when requirements.txt changes -------- ###
# Initiates the build-venv stage, copies the requirements and installs them in the virtual environment.
FROM build AS build-venv

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

### -------- Copy and run the script -------- ###
# Initiates a fresh stage, copying the installed dependencies from build-venv and setting PATH.
FROM python:3.13-slim AS run

ENV PATH="/venv/bin:$PATH"

COPY --from=build-venv /venv /venv
COPY . /fields

# Add a non-root user (security) and give him rights to edit the planet_trajectory folder
RUN addgroup --gid 12345 project_fields && \
    adduser --uid 12345 --gid 12345 --disabled-password --gecos "" project_fields && \
    chown -R 12345:12345 /fields/static/planet_trajectory

# Metadata injection. Add commit information and date/time to info.properties e.g.:
# build.version=sha-abc1234
# build.time=2026-09-27 08:15:00 UTC
ARG VERSION=unknown
RUN mkdir -p /fields && \
    { printf 'build.version=%s\n' "$VERSION"; \
      printf 'build.time=%s\n' "$(date -u '+%Y-%m-%d %H:%M:%S UTC')"; \
    } > /fields/info.properties


USER 12345
WORKDIR /fields
ENV PYTHONPATH="/fields"
EXPOSE 5000

CMD /venv/bin/gunicorn --workers ${WORKERS:-2} \
  --threads ${THREADS:-2} \
  --bind 0.0.0.0:5000 \
  --log-level ${LOG_LEVEL:-info} \
  --timeout ${TIMEOUT:-30} \
  wsgi:app
