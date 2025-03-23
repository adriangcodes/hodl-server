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

# Hosting

App hosted using Render via custom domain. Database hosted using Neon. Please refer to docs/user_guide.md for access details.

# Requirements

Please refer to requirements.txt for installed packages require to run this app.

# User Guide

Please refer to docs/user_guide.md for further details on access details and CRUD routes.

# ERD

Please refer to docs/erd.pdf for this project's ERD, as well as a justification for the database system selection.

# Feedback

Please refer to docs/feedback_log.md for feedback tracking.
Raw peer feedback for this project can be found in docs/feedback

# Third-Party Packages and Licenses

All third-party packages used are open source, and their use in this app can be considered ethical. No modifications have been made to their original code.

	1.	blinker==1.9.0 — MIT License https://github.com/jek/blinker/blob/main/LICENSE.txt
	2.	certifi==2025.1.31 — MPL-2.0 https://github.com/certifi/python-certifi/blob/main/LICENSE
	3.	charset-normalizer==3.4.1 — MIT License https://github.com/rs/charset_normalizer/blob/main/LICENSE
	4.	click==8.1.8 — BSD-3-Clause https://github.com/pallets/click/blob/main/LICENSE.rst
	5.	Flask==3.1.0 — BSD-3-Clause https://github.com/pallets/flask/blob/main/LICENSE.rst
	6.	flask-marshmallow==1.3.0 — MIT License https://github.com/marshmallow-code/flask-marshmallow/blob/dev/LICENSE
	7.	Flask-SQLAlchemy==3.1.1 — BSD-3-Clause https://github.com/pallets-eco/flask-sqlalchemy/blob/main/LICENSE.rst
	8.	idna==3.10 — BSD-like https://github.com/kjd/idna/blob/main/LICENSE.rst
	9.	itsdangerous==2.2.0 — BSD-3-Clause https://github.com/pallets/itsdangerous/blob/main/LICENSE.rst
	10.	Jinja2==3.1.6 — BSD-3-Clause https://github.com/pallets/jinja/blob/main/LICENSE.rst
	11.	MarkupSafe==3.0.2 — BSD-3-Clause https://github.com/pallets/markupsafe/blob/main/LICENSE.rst
	12.	marshmallow==3.26.1 — MIT License https://github.com/marshmallow-code/marshmallow/blob/dev/LICENSE
	13.	marshmallow-sqlalchemy==1.4.1 — MIT License https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/LICENSE
	14.	packaging==24.2 — Apache-2.0 or BSD-2-Clause https://github.com/pypa/packaging/blob/main/LICENSE
	15.	psycopg2-binary==2.9.10 — LGPL with exceptions https://github.com/psycopg/psycopg2/blob/master/LICENSE.txt
	16.	python-dotenv==1.0.1 — BSD-3-Clause https://github.com/theskumar/python-dotenv/blob/main/LICENSE
	17.	SQLAlchemy==2.0.39 — MIT License https://github.com/sqlalchemy/sqlalchemy/blob/main/LICENSE
	18.	typing_extensions==4.12.2 — Python Software Foundation License https://github.com/python/typing_extensions/blob/main/LICENSE
	19.	tzlocal==5.3.1 — MIT License https://github.com/regebro/tzlocal/blob/master/LICENSE.txt
	20.	urllib3==2.3.0 — MIT License https://github.com/urllib3/urllib3/blob/main/LICENSE.txt
	21.	Werkzeug==3.1.3 — BSD-3-Clause https://github.com/pallets/werkzeug/blob/main/LICENSE.rs
    22.	gunicorn==21.2.0 — MIT License https://github.com/benoitc/gunicorn/blob/master/LICENSE

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