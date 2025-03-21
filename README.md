# hodl-server

This project is my response to Coder Academy DEV1002 Assessment 3 - Databases and Servers.

This assessment follows on from my previous assessment submissions:
- hodl-app: a Python-based CLI app used to store Bitcoin holdings in CSV, and calculate current value and total gains/losses.
- hodl-data: a PostgreSQL-based relational database designed to manage cryptocurrency transactions and user wallets.

This Flask application is the core backend of a cryptocurrency wallet and tracking service. Its primary purpose is to manage user accounts, cryptocurrency and fiat currency data, digital wallets, and real-time or historical crypto prices. The app is built with modularity in mind, leveraging Flask Blueprints to separate and organise functionality into logical components—such as users, wallets, cryptocurrencies, fiat currencies, and pricing data.

By registering different blueprints, the app allows for scalable development and maintenance of API routes related to each data domain. For example, user-related routes are handled in users_bp, while cryptocurrency prices are managed via cryptoprices_bp. The app also includes a global error handler for validation errors, ensuring consistent and user-friendly error messages for incorrect input. This makes it robust for integration with frontend applications or third-party clients that require reliable data interaction.

This app serves as the foundation of a flexible crypto-related backend service—capable of supporting features like portfolio tracking, currency conversion, and user wallet management, with clear separation of concerns and scalable architecture. Similar to previous assessments, future work would look to combine and refine hodl-app, hodl-data and hodl-server with front-end design, to create a Bitcoin wallet/exchange MVP.

# GitHub

GitHub repo for this assessment: https://github.com/adriangcodes/hodl-server

GitHub repo for past assessments:
- hodl-app: https://github.com/adriangcodes/hodl-app
- hodl-data: https://github.com/adriangcodes/hodl-data

# User Guide

Please refer to docs/user_guide.md

# ERD

The ERD for this project can be found in docs/erd.pdf

# Feedback

Please reference docs/feedback_log.md for feedback tracking.
Raw peer feedback for this project can be found in docs/feedback

# References

Dev.to, 2021. Using .env files for environment variables in Python applications. [online] Available at: https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1 [Accessed 21 Mar. 2025].

GeeksforGeeks, 2023. How to create and use .env files in Python? [online] Available at: https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/ [Accessed 21 Mar. 2025].

Medium, 2020. Sommer, J., How to serialize and validate your data with Marshmallow. [online] Available at: https://medium.com/@jesscsommer/how-to-serialize-and-validate-your-data-with-marshmallow-a815b2276a [Accessed 21 Mar. 2025].

ObjectRocket, 2019. Python error handling with the Psycopg2 PostgreSQL adapter. [online] Available at: https://kb.objectrocket.com/postgresql/python-error-handling-with-the-psycopg2-postgresql-adapter-645 [Accessed 21 Mar. 2025].

Psycopg.org, 2023. psycopg2.errors — Exception hierarchy. [online] Available at: https://www.psycopg.org/docs/errors.html [Accessed 21 Mar. 2025].

Python Software Foundation, 2024a. datetime — Basic date and time types. [online] Available at: https://docs.python.org/3/library/datetime.html [Accessed 21 Mar. 2025].

Python Software Foundation, 2024b. re — Regular expression operations. [online] Available at: https://docs.python.org/3/library/re.html [Accessed 21 Mar. 2025].

Read the Docs, 2024. marshmallow.validate. [online] Available at: https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html [Accessed 21 Mar. 2025].

SQLAlchemy, 2024. Column and data types — SQLAlchemy 2.0 Documentation. [online] Available at: https://docs.sqlalchemy.org/en/20/core/type_basics.html [Accessed 21 Mar. 2025].

Stack Overflow, 2016. Flask-SQLAlchemy numeric type. [online] Available at: https://stackoverflow.com/questions/39420754/flask-sqlalchemy-numeric-type [Accessed 21 Mar. 2025].