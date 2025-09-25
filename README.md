# Stephanie Forcier - Hologram Coding Interview

## Overview
This project is part of the technical coding portion of Hologram's interview cycle. The full set of instructions can be found here: https://www.notion.so/teamhologram/Full-Stack-Engineering-Exercise-24833577b6b680a38760ddc5729b5cff
Here is a TLDR of this project:

In this project, I will create an application that should accept a CDR (call detail record) file with usage strings. 
The app will parse the strings properly and save the data to a database.
This project also consists of a user-facing application where users can:
Upload a CDR file
Display the parsed and normalized records in a table

This project must also be containerized, with details for how to start and use it.

## Technologies
This project uses the following technologies:
- Poetry - package management
- Flask (Python) - backend
  - flask-restful for REST API package
- Vue (JavaScript) - frontend
  - Axios package for making API calls
  - Vite for packaging
- MongoDB for noSQL database
  - flask-pymongo for database driver

TODO:
- Save the parsed data to a DB
- Create a view that will display the data
- Set up the project to be containerized and easily started
- Write tests!
- Add validation to data, sanitize and prevent SQL injection/other attacks
- Add custom exception handling for smoother errors

IMPROVEMENTS:
- Make process async
- More friendly UI - single page? Keep multiple pages?
- Swagger-style API UX
- Future milestone: editing/updating records, more details about what happens if you save an existing record, etc