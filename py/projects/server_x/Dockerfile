FROM python:3.11-slim

RUN useradd --create-home --uid 1234 appuser
USER 1234

ENV PATH="${PATH}:/home/appuser/.local/bin"

RUN python3 -m pip install --user pipx
RUN python3 -m pipx ensurepath

RUN pipx install poetry==1.8.1

RUN poetry config virtualenvs.in-project true

WORKDIR /home/appuser/py/projects/server_x

COPY --chown=appuser ./py/projects/server_x/pyproject.toml  /home/appuser/py/projects/server_x/
COPY --chown=appuser ./py/projects/server_x/poetry.lock     /home/appuser/py/projects/server_x/
RUN poetry install --only main --no-root --no-directory

COPY --chown=appuser ./py/libs                        /home/appuser/py/libs
COPY --chown=appuser ./py/projects/server_x/server_x  /home/appuser/py/projects/server_x/server_x
RUN poetry install --only main

# More or less the same as activating the virtual env that poetry creates
ENV VIRTUAL_ENV=/home/appuser/py/projects/server_x/.venv
ENV PATH $VIRTUAL_ENV/bin:$PATH

CMD python server_x/fastapi_app.py