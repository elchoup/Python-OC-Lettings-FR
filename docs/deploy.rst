Deploy process
==============

Deploy with Github Actions and Render

______________________________________

The deploy process has been automatised with a CI/CD pipeline thanks to
Github actions.
Here is the differents tasks it does on each push or pull request

1. Code validation:
The first step runs on all branches.
We make a flake8 validation and a test coverage validation.
Tests must have a minimum coverage of 80%.

2. Build and push of Docker image:
The docker image is automaticly build and push on the docker hub 
every time a push on main branch is made.

3. Render deploy:
After push and build of docker image, a request is send to render 
to trigger a new deployment using the new docker image.