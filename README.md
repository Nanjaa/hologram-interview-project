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
  - Vite for compiling
  - PrimeVue for UI Suite
- MongoDB for noSQL database
  - flask-pymongo for database driver

## TODO:
- Set up the project to be containerized and easily started
- Write tests!
- Add custom exception handling for smoother errors

## IMPROVEMENTS AND PROPOSED FUTURE MILESTONES:
- Make process async
- Swagger-style API UX
- Future milestone: editing/updating records, more details about what happens if you save an existing record, etc
- Restrict what data loads to the current user
- Add pagination to CDR table
- Configure a linter to properly format the code and make everything ~pretty~
- There is a latency problem with the fetch all query
- Add validation to data, sanitize and prevent SQL injection/other attacks