FROM python:3.11-slim

WORKDIR /app

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}

#Install pipenv

RUN pip install pipenv


# Copy pipfile and pipfile.lock to install dependencies

COPY Pipfile Pipfile.lock ./

# Install all dependencies without creating a venv

RUN pipenv install --deploy

# Copy all project content

COPY . .

# Collect statics

RUN pipenv run python manage.py collectstatic --noinput


# Expose django default port
EXPOSE 8000

# Command to start app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]