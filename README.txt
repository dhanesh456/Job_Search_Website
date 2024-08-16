## README.txt

## Student Information: Student ID: S4000700; Name: Dhanesh Gaikwad

#Preface
Part of RMIT University's Advanced Programming for Data Science course, COSC2820/2815, includes this project. Two benchmarks make up the task. Several machine learning models were developed in Milestone I to classify job adverts using various document vector representations. Milestone II involves using the Flask web framework to create a job search website.

## Overview of the project
In addition to letting companies post fresh job ads, the job search website lets job seekers peruse already-published job ads. It makes recommendations for new job categories for job adverts using a machine learning model that was trained in Milestone I. By enhancing the user experience overall, this feature lowers the possibility of human error and increases job exposure to qualified candidates.


#Features

### For Job Searchers: - **Search for Jobs:** Keyword-based job listing searches are available to users. For thorough search results, keyword strings in comparable forms (such as "work", "works", and "worked") are supported by the search capability.
**Previews of Jobs:** A list of relevant job advertisement previews for the supplied term is displayed in the search results.
- **Work Specifics:** Clicking on a job ad preview allows users to read the entire job description.

### For Employers: - **Create New Job Listing:** Employers can add details such a title, description, pay, and other details to create new job listings.
- **Suggested Category:** The job description and/or title are used by the website to suggest a list of categories for new job ads. If necessary, employers are able to override the suggested categories.
- **Job Data Management:** The generated job advertisement can be accessed through a suitable search or URL and is part of the job data.


## Organizational Framework
Below are the files and directories that make up the project:
*app.py:** All routes and functionality are contained in the main Flask application file.
HTML templates for the home, search results, job details, and create job pages are located in the **templates/:** directory.
-**static/:** directory with static files, like CSS, that are used to style webpages.
**data/:** - Job data files in a directory that is used to show off the features.

3. Run the Flask application:

4. To access the job search website, open a web browser and navigate to `http://127.0.0.1:5000/}.

## Important Information - **Model Path:** Verify that the `app.py` file's designated path leads to the pre-trained machine learning model file ({descFT_LR.pkl}).
**Data Folder:** In order for the application to load and process the job data files, they must be placed in the `data/} directory.
