from flask import Flask, render_template, request, redirect, url_for, jsonify
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import os
import joblib

# Initializing the Flask application
app = Flask(__name__)

# Function to load job data from text files in a specified folder
def load_job_data(data_folder):
    job_data = []
    for subdir, _, files in os.walk(data_folder):
        category = os.path.basename(subdir)  # Getting the category name from the folder name
        for file in files:
            if file.endswith(".txt"):  # Processing only text files
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    job_data.append((f.read(), category))  # Appending job content and category as a tuple
    return job_data

# Function to preprocess text by tokenizing, lowercasing, and stemming the words
def preprocess_text(text):
    stemmer = PorterStemmer()
    tokens = word_tokenize(text.lower())  # Tokenizing and converting to lowercase
    stemmed_tokens = [stemmer.stem(token) for token in tokens]  # Applying stemming to each token
    return ' '.join(stemmed_tokens).strip()  # Joining the stemmed tokens back into a single string

# Loading job data from the specified folder
data_folder = 'data'
job_data = load_job_data(data_folder)
preprocessed_data = [preprocess_text(job[0]) for job in job_data]  # Preprocessing the job descriptions

# Loading the pre-trained machine learning model for recommending job categories
model_path = "E:/RMIT/Semester_2/Advanced Programming for Data Science (2410)/Assignments/Assignment2.2/job_search_website/models/descFT_LR.pkl"
model = joblib.load(model_path)

# Function to recommend categories based on the job description
def recommend_categories(description):
    preprocessed_desc = preprocess_text(description)  # Preprocessing the description
    if preprocessed_desc.strip() == "":
        return ["Uncategorized"]  # Returning "Uncategorized" if the description is empty
    categories = model.predict([preprocessed_desc])  # Using the model to predict categories
    return categories

# Function to parse job details from a job description string
def parse_job_details(job):
    details = {}
    lines = job.split('\n')  # Splitting the job string into lines
    for line in lines:
        if line.startswith("Title:"):
            details['title'] = line.replace("Title:", "").strip()  # Extracting the job title
        elif line.startswith("Company:"):
            details['company'] = line.replace("Company:", "").strip()  # Extracting the company name
        elif line.startswith("Webindex:"):
            details['webindex'] = line.replace("Webindex:", "").strip()  # Extracting the web index
        elif line.startswith("Description:"):
            details['description'] = line.replace("Description:", "").strip()  # Extracting the job description
        elif line.startswith("Salary:"):
            details['salary'] = line.replace("Salary:", "").strip()  # Extracting the salary
    return details

# Function to search for jobs based on a keyword
def search_jobs(keyword, job_data, preprocessed_data):
    stemmer = PorterStemmer()
    keywords = [stemmer.stem(k.lower()) for k in keyword.split()]  # Stemming the keywords
    
    matched_jobs = []
    for i, (job, category) in enumerate(zip(preprocessed_data, job_data)):
        if all(k in job for k in keywords):  # Checking if all keywords are in the job description
            job_details = parse_job_details(job_data[i][0])
            job_details['id'] = i  # Adding job ID for linking to details
            job_details['category'] = job_data[i][1]  # Adding category
            matched_jobs.append(job_details)
    return matched_jobs

@app.route('/')
def index():
    # Rendering the home page template
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    # Getting the search keyword from the request
    keyword = request.args.get('keyword') if request.method == 'GET' else request.form['keyword']
    print(f"Searching for keyword: {keyword}")  # Debugging statement
    matched_jobs = search_jobs(keyword, job_data, preprocessed_data)  # Searching for jobs
    num_results = len(matched_jobs)
    print(f"Number of results: {num_results}")  # Debugging statement
    return render_template('search.html', num_results=num_results, keyword=keyword, matched_jobs=matched_jobs)

@app.route('/job/<int:job_id>')
def job_details(job_id):
    # Fetching details for a specific job ID
    print(f"Fetching details for job ID: {job_id}")  # Debugging statement
    if 0 <= job_id < len(job_data):
        job = job_data[job_id][0]
        category = job_data[job_id][1]
        job_details = parse_job_details(job)
        job_details['category'] = category
        keyword = request.args.get('keyword')
        return render_template('job_details.html', job_details=job_details, keyword=keyword)
    else:
        print(f"Invalid job ID: {job_id}")  # Debugging statement
    return redirect(url_for('index'))

@app.route('/recommend_categories', methods=['POST'])
def recommend_categories_route():
    # Getting the job description from the request and recommending categories
    data = request.get_json()
    description = data.get('description', '')
    print(f"Description received for recommendation: '{description}'")  # Debugging statement
    categories = recommend_categories(description)
    return jsonify({'categories': categories})

@app.route('/create', methods=['GET'])
def create_job():
    # Rendering the create job listing page
    return render_template('create_job.html')

@app.route('/create', methods=['POST'])
def save_job():
    # Saving a new job listing
    title = request.form['title']
    company = request.form['company']
    description = request.form['description']
    salary = request.form['salary']
    
    # Ensuring salary is a number
    try:
        salary = float(salary)
    except ValueError:
        return "Salary must be a number", 400
    
    categories = request.form.get('categories', '')
    
    if not categories:
        categories = recommend_categories(description)
    else:
        categories = categories.split(',')

    job_details = {
        'title': title,
        'company': company,
        'description': description,
        'salary': salary,
        'categories': categories
    }

    print(f"Adding new job: {job_details}")  # Debugging statement
    new_job_entry = f"Title: {title}\nCompany: {company}\nWebindex: {len(job_data)}\nDescription: {description}\nSalary: {salary}"
    job_data.append((new_job_entry, categories))
    preprocessed_data.append(preprocess_text(new_job_entry))  # Preprocess and add the new job entry
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Starting the Flask application
    app.run(debug=True)


# Flask: Grinberg, M. (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly Media.
#        https://www.oreilly.com/library/view/flask-web-development/9781491991732/

# NLTK (Natural Language Toolkit): Bird, S., Klein, E., & Loper, E. (2009). Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit. O'Reilly Media.
#        https://www.oreilly.com/library/view/natural-language-processing/9780596803346/

# joblib: Joblib Development Team. (2023). Joblib: Python Library for Efficiently Managing Large Datasets and Computing. Retrieved from https://joblib.readthedocs.io/
#        https://joblib.readthedocs.io/

# Porter Stemmer: Porter, M. F. (1980). An algorithm for suffix stripping. Program, 14(3), 130-137.
#        https://www.tandfonline.com/doi/abs/10.1080/00330398009382197

# Natural Language Processing (General): Jurafsky, D., & Martin, J. H. (2021). Speech and Language Processing (3rd ed.). Prentice Hall.
#        https://web.stanford.edu/~jurafsky/slp3/

# Python Programming Language: Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. CreateSpace.
#        https://docs.python.org/3/reference/

# os module (Python standard library): Python Software Foundation. (2023). os — Miscellaneous operating system interfaces. Retrieved from https://docs.python.org/3/library/os.html
#        https://docs.python.org/3/library/os.html

# word_tokenize function (NLTK): Bird, S., Klein, E., & Loper, E. (2009). Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit. O'Reilly Media.
#        https://www.oreilly.com/library/view/natural-language-processing/9780596803346/

# Scikit-learn (used within joblib for model handling): Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.
#        https://www.jmlr.org/papers/v12/pedregosa11a.html
