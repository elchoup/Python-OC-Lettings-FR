Description 
===========


Python OC Lettings is a web application designed to manage 
property lettings. It allows handling users, lettings, addresses, and user profiles. 
The application is built using the Django ORM.

The app offers three main functions: : 

    . Manage Lettings: Each letting has a detailed address, 
    and users can view the specific details of each letting.

    . Handle Addresses: Lettings addresses include details such as number, 
    street, city, state, zip code, and country ISO code.

     .Handle Profiles: Every app user can have a user profile that stores their personal information.

The application uses Django's models for the database structure and HTML templates for the user interface. 
It is designed to be deployed on Render using Docker images and supports a CI/CD pipeline for continuous integration and delivery.