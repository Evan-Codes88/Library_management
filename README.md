# **Library Management System (LMS) API**

A simple but robust API used to manage a Library's operations. This includes books, members and loans. This system streamlines library management in a sense of tracking available books, member details, and loan records.

---

## Table of Contents
- [Purpose](#purpose)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
  - [How to Clone the Repository](#How-to-Clone-the-Repository)
  - [Setting up the Virtual Environment (venv)](#setting-up-the-virtual-environment-venv)
  - [Activating the Virtual Environment](#activating-the-virtual-environment)
  - [Installing the Required Packages](#installing-the-required-packages)
  - [Required Packages](#required-packages)
- [Prerequisites](#Prerequisites)
  - [How to Run the API Locally](#how-to-run-the-api-locally)
- [Web Server Deployment](#Web-Server-Deployment)
  - [HTTP Status Codes](#http-status-codes)
- [Licensing and Legal/Ethical Impacts](#licensing-and-legalethical-impacts)
   - [License Overview](#license-overview)
   - [Full MIT License Text](#full-mit-license-text)
   - [Ethical Considerations](#ethical-considerations)
- [Explanation of Chosen Database System](#explanation-of-chosen-database-system)
   - [Key Features of RDBMS](#key-features-of-rdbms)
   - [Comparison to Other Database Systems](#comparison-to-other-database-systems)
   - [Entity Relationship Diagram](#entity-relationship-diagram)
   - [Conclusion](#conclusion)
   - [Feedback](#feedback)
- [Credits](#credits)


## **Purpose**

This Library Management System (LMS) is designed to simplify the administrative tasks of librarians. It allows staff to effeciently manage book collections, member data, loan records and streamlines proccesses for efficiency.

## **Features**

- **Book Management:** Add, update, delete and search for books or authors.

- **Member Management:** Manage library member records.

- **Loan Tracking:** Monitor active loans by their borrow and return dates.

- **Real-Time Availablility:** Automatically update available copies when books are borrowed.

- **Database Integration:** Uses SQLAlchemy for robust database management.



## **System Requirements**

- **Python Version:** 3.9.6 or later  
- **Database:** PostgreSQL recommended  
- **Operating System:** Windows, macOS, or Linux



## **Installation**
<br>

## How to Clone the Repository

To clone the Library Management repository to your local machine, follow the steps below:

### Steps to Clone

1. **Open a Terminal or Command Prompt**  
   Open your terminal, command prompt, or any CLI tool you use for development.

2. **Navigate to the Directory Where You Want to Clone the Repository**  
   Use the `cd` command to navigate to your desired folder. For example:
   ```cd path/to/your/directory```

3. **Clone The Repository**
  Run the following command to clone the repository:
  ```git clone https://github.com/Evan-Codes88/Library_management.git```

4. **Navigate To The Cloned Repository**
  Once the cloning process is complete, navigate into the cloned repository folder:
  ```cd Library_management```

5. **Switch To The Main Branch**
  Ensure you are on the main branch:
  ```git checkout main```

6. **Open The Project In Your Code Editor**
  If you're using Visual Studio Code, you can open the project by running:
  ```code .```

### **Setting up the Virtual Environment (venv)**

1. Open your terminal or command prompt.
2. Navigate to your project directory:
   ```bash
   cd /path/to/your/project
   ```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activating the Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Installing the Required Packages

Once the virtual environment is activated, install the necessary packages:

```bash
pip install -r requirements.txt
```

Alternatively, install each package individually:

```bash
pip install blinker==1.9.0 click==8.1.7 Flask==3.1.0 flask-marshmallow==1.2.1 Flask-SQLAlchemy==3.1.1 greenlet==3.1.1 importlib_metadata==8.5.0 itsdangerous==2.2.0 Jinja2==3.1.4 MarkupSafe==3.0.2 marshmallow==3.23.1 marshmallow-sqlalchemy==1.1.0 packaging==24.2 psycopg2==2.9.10 python-dotenv==1.0.1 SQLAlchemy==2.0.36 typing_extensions==4.12.2 Werkzeug==3.1.3 zipp==3.21.0
```

## Required Packages

- **blinker:** 1.9.0  
- **click:** 8.1.7  
- **Flask:** 3.1.0  
- **flask-marshmallow:** 1.2.1  
- **Flask-SQLAlchemy:** 3.1.1  
- **greenlet:** 3.1.1
- **gunicorn:** 23.0.0
- **importlib_metadata:** 8.5.0  
- **itsdangerous:** 2.2.0  
- **Jinja2:** 3.1.4  
- **MarkupSafe:** 3.0.2  
- **marshmallow:** 3.23.1  
- **marshmallow-sqlalchemy:** 1.1.0  
- **packaging:** 24.2  
- **psycopg2:** 2.9.10  
- **python-dotenv:** 1.0.1  
- **SQLAlchemy:** 2.0.36  
- **typing_extensions:** 4.12.2  
- **Werkzeug:** 3.1.3  
- **zipp:** 3.21.0  

## **Prerequisites**

**Before running the API for the first time, ensure the following steps are completed:**

---

### **Set Up PostgreSQL Database**

1. Create a new database in PostgreSQL:

   ```sql
   CREATE DATABASE lms_api;
   ```
2. Define a DATABASE_URI in your ```.env``` file
  an example looks like this:
    ```bash
    DATABASE_URI=postgresql://username:password@localhost:5432/lms_api
    ```
    <br>
    Replace username, password, and localhost with your postgreSQL credentials.

### **Initialize the Database Tables**

Use Flask CLI commands to create the necessary tables:

```bash
flask db create # This creates your entity tables
flask db seed # This seeds all of the sample data
flask db drop # This will drop all tables and relations
```

### How to Run the API Locally

1. Ensure your virtual environment is activated.
2. Start the API server:
   ```bash
   flask run
   ```
3. Access the API at `http://localhost:8080`.

---

## Testing The API Locally With Insomnia

Insomnia is a powerful REST client that allows you to test your API endpoints with a user-friendly interface. Here's how to set up and use Insomnia to test your Library Management System (LMS) API locally.

**1. Install Insomnia**
If you haven't already, download and install Insomnia from the official website:
[Download Insomnia](#https://insomnia.rest/download)
<br>

**2. Set Up Insomnia**
Once Insomnia is installed, follow these steps to set it up for testing your API locally:

- ***Open Insomnia:*** Launch the Insomnia application. (Click 'Use Local Scratchpad')
- ***Create a New Request:***
  - Click on the New Request button.
  - Give your request a name (e.g., "Get All Books").
  - Select the appropriate HTTP method (e.g., GET, POST, PATCH, PUT, DELETE) from the dropdown menu next to the request name.
- **Configure API Requests:**
  For each type of API request (GET, POST, PUT, PATCH, DELETE), follow the instructions below to configure them in Insomnia.
  - **GET:**
    For a GET request to fetch all books from the API:
    - In the request setup window, set the method to GET.
    - Enter the URL for the request:
      http://localhost:8080/books
    - Click Send.
    - This will display all of the books within the database in JSON format.
    <br>
  - **GET from ID:**
    For a GET from ID request to fetch one book from the API:
    - In the request setup window, set the method to GET.
    - Enter the URL for the request:
      http://localhost:8080/books/1 (Use ID of book you want to see)
    - Click Send.
    - This will display the book in JSON format.
  - **POST:**
    To create a new book with a POST request:
    - Set the method to POST.
    - Enter the URL:
      http://localhost:8080/books
    - Go to the Body tab and select JSON.
    - Add the JSON data for the new book
    - Click Send
  - **PUT:**
    To update an existing book with a PUT request:
    - Set the method to PUT.
    - Enter the URL with the book ID:
      http://localhost:8080/books/1
    - Go to the Body tab and select JSON.
    - Add the JSON data to update the book details (All details required for PUT method)
    - Click Send
  - **PATCH:**
    To update a book's title using a PATCH request:
    - Set the method to PATCH.
    - Enter the URL with the book ID:
      http://localhost:8080/books/1
    - Go to the Body tab and select JSON.
    - Add the JSON data to update the book's title
    - Click Send
  - **DELETE:**
    To delete a book using a DELETE request:
    - Set the method to DELETE.
    - Enter the URL with the book ID:
      http://localhost:8080/books/1
    - Click Send.

- **Viewing Response And Status Code:**
  After sending the request, you will see the response in the lower section of Insomnia:
  - The status code (e.g., 200, 201, 404) will be displayed at the top of the response window.
  - The response body will appear below the status code, showing the data returned from the server.

- **Testing Other API Endpoints:**
  To test other resources such as authors, genres, loans, or members, simply change the endpoint in the URL:
  - For authors: http://localhost:8080/authors
  - For genres: http://localhost:8080/genres
  - For loans: http://localhost:8080/loans
  - For members: http://localhost:8080/members

  Make sure to adjust the request method and body accordingly for each type of operation (GET, POST, PUT, PATCH, DELETE).
<br>

By following these steps, you can easily test your API locally using Insomnia and ensure everything is functioning correctly before deploying it to a live server.
---

### **Web Server Deployment:**
<br>
The live deployment of the Library Management System (LMS) API is hosted on Render:

**URL:** https://evan-library-management-system.onrender.com
<br>

***How To Use The Deployment:***
You can interact with the API through various HTTP requests (GET, POST, PUT, PATCH, DELETE) to manage library resources, such as books, authors, genres, loans, and members.

***CRUD Operations Examples:***

- GET: Retrieve Resources

  - Example - Fetch All Books:
    ```
    curl -X GET https://evan-library-management-system.onrender.com/books
    ```

    Expected Response:
      ```
      [
        {
          "id": 1,
          "title": "Book Title",
          "isbn": "ISBN NO.",
          "available_copies": "Number of copies available",
          "author_id": "Author ID",
          "genre_id": "Genre ID"
        }
      ]
      ```
<br>

- POST: Create A New Resource (This following command is done within your terminal or command prompt)

  - Example - Create New Book:
    ```
    curl -X POST POST https://evan-library-management-system.onrender.com/books \
    -H "Content-Type: application/json" \
    -d '{"title": "New Book", "isbn": "isbn number", "available_copies": "Number of copies available", "author_id": "author id", "genre_id": "genre id"}'
    ```

    ***This command:***

    - POST: Specifies the HTTP method to create a new resource.
    - URL: Points to your API endpoint (/books).
    - Headers: Includes the Content-Type: application/json to tell the
    server the request is in JSON format.
    - Data: Provides the JSON body of the request, which includes the book's details.
    
    ***Execute the Command:***
      Press Enter to execute it.

    Expected Response:
      ```
      {
        "message": "Book added successfully",
        "book": {
          "id": 2,
          "title": "New Book",
          "isbn": "ISBN NO.",
          "available_copies": "Number of copies available",
          "author_id": "Author ID",
          "genre_id": "Genre ID"
        }
      }
      ```

- PATCH: Partially Update An Existing Resource

  - Example - Update A Book's Name:
    ```
    curl -x PATCH https://evan-library-management-system.onrender.com/books/1 \
    -H "Content-Type: application/json" \
    -d '{"title": "Book 1 Updated"}'
    ```
    ***This command:***

    - PATCH: Specifies the HTTP method to partially update a new resource.
    - URL: Points to your API endpoint (/books/1).
    - Headers: Includes the Content-Type: application/json to tell the
    server the request is in JSON format.
    - Data: Provides the JSON body of the request, which includes the book's details used to update.

    Expected Response:
    ```
    {
      "message": "Book updated successfully",
      "book": {
        "id": 1,
        "title": "Updated Title",
        "isbn": "ISBN NO",
        "available_copies": "Number of copies available",
        "author_id": "Author ID",
        "genre_id": "Genre ID"
      }
    }
    ```

- PUT: Update An Existing Resource (All fields required)

  - Example - Update A Book's Details:
    ```
    curl -x PUT https://evan-library-management-system.onrender.com/books/1 \
    -H "Content-Type: application/json" \
    -d '{"title": "Updated Title", "isbn": "Updated ISBN", "available_copies": "Updated Copies", "author_id": "Updated author id", "genre_id": "Updated genre id"}'
    ```
    ***This command:***

    - PUT: Specifies the HTTP method to completely update a new resource.
    - URL: Points to your API endpoint (/books/1).
    - Headers: Includes the Content-Type: application/json to tell the
    server the request is in JSON format.
    - Data: Provides the JSON body of the request, which includes the book's details used to update.

    Expected Response:
    ```
    {
      "message": "Book updated successfully",
      "book": {
        "id": 1,
        "title": "Updated Title",
        "isbn": "Updated ISBN NO",
        "available_copies": "Updated Number of copies available",
        "author_id": "Updated Author ID",
        "genre_id": "Updated Genre ID"
      }
    }
    ```

- DELETE: Remove A Resource

  - Example - Delete A Book:
    ```
    curl -X DELETE https://evan-library-management-system.onrender.com/books/1
    ```

    Expected Response:
    ```
    {
      "message": "Book deleted successfully"
    }
    ```
<br>

---

## HTTP Status Codes

HTTP status codes indicate the result of the API request. Below are common status codes you might encounter when interacting with the Library Management System (LMS) API:

**200 OK**
The 200 OK status code indicates that the request was successful, and the server has returned the requested data.
<br>

**201 CREATED**
The 201 Created status code indicates that the request was successful and resulted in the creation of a new resource.
<br>

**404 NOT FOUND**
The 404 Not Found status code indicates that the requested resource could not be found on the server.
<br>

---

## Licensing and Legal/Ethical Impacts

### License Overview

### Key Points of the MIT License:
- **Permission:** You are permitted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.
- **Attribution:** You must include the original copyright notice and the MIT License text with any distribution.
- **Warranty Disclaimer:** The software is provided "as is," without warranty of any kind. The authors are not liable for any damages or issues arising from the use of the software.

### Full MIT License Text:

```
MIT License

Copyright (c) 2024 Evan Meehan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Ethical Considerations

The LMS API should be used responsibly, adhering to legal and ethical standards:
- **Data Privacy:** Ensure that sensitive information, such as user data and borrowing history, is securely handled and stored.
- **Compliance:** Follow local laws and regulations when deploying and using the system.
- **Community Impact:** Promote responsible usage in educational and public institutions to benefit communities without causing harm or bias.

---

For more information about licensing, visit [Open Source Initiative](https://opensource.org/licenses/MIT).




## Explanation of Chosen Database System

The database system I have chosen for this Library Management System (LMS) is a **Relational Database Management System (RDBMS)**. 

### Key Features of RDBMS:

**Structured Data Storage:**  
Data is stored within tables (relations) with rows and columns. Each table represents a different entity. In my case, I have tables for **Author**, **Genre**, **Book**, **Member**, and **Loan**. Each row within these tables represents a record.

**Primary and Foreign Keys:**  
- **Primary Keys (PK):** These keys ensure each record is unique.  
- **Foreign Keys (FK):** These keys establish relationships between tables, making it easy to connect different entities.

**Normalization:**  
Normalization reduces redundancy by organizing data into tables based on related entities. This ensures data is easily updated, consistent, and avoids duplication.

**SQL (Structured Query Language):**  
RDBMS use SQL to query, manipulate, and manage data. SQL is also used for creating and retrieving records, and defining relationships between records. For this assignment, I will be using **PostgreSQL**.

**ACID Properties:**  
ACID (Atomicity, Consistency, Isolation, Durability) properties guarantee that transactions are reliable and prevent data corruption.

---



### Comparison to Other Database Systems:

**Relational Database vs. NoSQL Database:**  

- **Structure:**  
  RDBMS store data within structured tables, whereas NoSQL databases store data in flexible, unstructured formats like graphs, dictionaries, or documents.  

- **Schema:**  
  RDBMS require a predefined schema with strict relationships. NoSQL databases do not have a schema and allow for dynamic data models.  

- **Scalability:**  
  RDBMS scale vertically, meaning more power is added to a single server. NoSQL databases scale horizontally, adding more servers to the system.  

- **Use Case:**  
  NoSQL is often used for large-scale applications, while RDBMS are generally used for structured data with fixed relationships.  


### Conclusion:
For the Library Management System, a **relational database** is the optimal choice. It provides a solid foundation for managing structured data, ensuring clear relationships between entities, maintaining data integrity, and supporting complex queries.

---


## **Entity Relationship Diagram:**

![ERD IMAGE](erd.png)


---

### Feedback

Who: Taner Maddocks\
When: 6/12/24\
What Document: README.md\
Feedback:
<br>
***Strengths***

- Very well structured document, easy to navigate and read.

- Description of the application leaves nothing to be confused about in terms of its function.

- Dependencies installation is easy to follow.

- Your Explanation of Chosen Database section and Licensing and Legal/Ethical impacts section are both well-structured.

***Areas for improvement***

- When describing the first run of the application, you don't describe the necessity to create the database in postgreSQL or the steps to use the cli commands to create the tables.

- Linked to that, is that the user would need to define their own DATABASE_URI, which would require instruction.

- Only other nitpick is that you have your Required Packages section separate from the instructions to install said packages.

***Action Taken:***
- Updated Prerequisites to explain how to initialise database and use CLI commands
- Explained how to define DATABASE_URI and what file to do so
- Moved required packages to be in the same section as install packages

***Justification***
- A critical step for the first run of the application is to set up the database properly. Without clear instructions on initializing the PostgreSQL database and creating tables using CLI commands, users might struggle to get the application running. Adding this to the "Prerequisites" section ensures users are prepared before running the app and reduces confusion. It improves usability and makes the setup process self-contained and complete.
```Providing commands like flask db init or SQL scripts ensures all necessary database setup actions are easy to follow.```
- The DATABASE_URI is essential for connecting to the database, and it needs to be user-specific (e.g., username, password, host, and database name). Without clear guidance on:
  - Where the DATABASE_URI needs to be defined (e.g., config.py or .env file).
  - How to format the connection string properly (e.g., postgresql://user:password@localhost/dbname), users might not know how to proceed.
Providing this explanation makes the application setup developer-friendly and removes ambiguity.
- Having the "Required Packages" section separate from the installation steps creates unnecessary fragmentation and can disrupt the user’s flow when setting up the application.


<br>

Who: Brendon A\
When: 12/12/24\
What Document: README.md\
Feedback:
<br>
Reviewing your ERD, maybe you can expand or briefly explain its relationship in the README? e.g. explain why author to books has a mandatory one to many relationship? As i was thinking, in your database design, an author can exist without a book because the Author table does not depend on the Book table for its existence. i.e. On the Author side, it would have double lines (||) indicating that one author can exist without necessarily having written any books. On the Book side, it would have a zero or many notation (0..*) indicating that a book must have one and only one author but one author can write zero or many books. If not, an explanation would be good to explain.

Your database explanation on why it is chosen and comparison is succinct and clear. However, additions of example would be nice to expand a little more for ease of understanding for different types of users (especially for beginners trying to comprehend databases). For instance, under normalisation, while the normalisation is explained i.e. it reduces redundancy etc, an example like "For instance, instead of storing author information repeatedly in the Book table, you have a separate Author table linked to the Book table through author_id." would be good.

Nevertheless, your readme is comprehensive and easy to navigate with the table of content as a good addition. Ethical considerations were also added exemplifying that you give this project a thorough thought including its legal implications. I could only think of one simple addition for your readme installation guide: maybe you can add instructions for cloning the repository if users are starting from scratch? Otherwise, really great work!

***Action Taken:***

  - My relationship between author and book stayed the same as a book cannot exist without an author and an author cannot exist without writing a book.

  - Expanded on the normalization within my README.md

  - Added instructions on how to clone repository.

***Justification***

  - I decided to keep the relationship mandatory for both entities because it reflects the logical constraints of your domain. A book inherently requires an author for it to exist, as authorship is fundamental to the concept of a book. Conversely, in your design, an author must have written at least one book, emphasizing that only authors with published works are relevant to your system.

  This decision aligns with a stricter interpretation of business rules, ensuring that every author in your database is actively tied to a book, which may simplify queries and avoid unnecessary null values. However, you I was open to critique, which is why providing an explanation in the README was important. Adding this rationale clarified my choice to users, preventing misunderstandings and showing thoughtful database modeling.

  - While my original explanation of normalization was sufficient, expanding on it with a practical example made the concept more accessible to beginners. Database normalization can be abstract, so illustrating how it reduces redundancy (e.g., avoiding repeated author information in the Book table) grounds the concept in reality.

  This improvement helps users of varying skill levels, aligning with a user-centered approach. It also demonstrates my commitment to making my README a learning resource, not just a technical document, which adds value to my project.

  - Adding repository cloning instructions ensures my README supports users who may be new to working with version control systems like Git. By guiding them through the process of setting up the project from scratch, I lower the barrier to entry for anyone interested in using or contributing to my project. This step enhances accessibility and aligns with best practices for open-source projects, further reflecting the inclusive nature of my documentation.


<br>

Who: Chris A\
When: 14/12/24\
What Document: Member.py\
Feedback:
<br>
**Strengths:**

Your Member model and schema are well-structured, demonstrating a solid grasp of Flask, Marshmallow, and database modelling. The validate_date_range function is particularly well-implemented, enforcing constraints on the join_date field with clear, user-friendly error messages. Marshmallow’s validators for name, membership_number, and email enhance data integrity, while the custom error messages improve usability. Including a Meta class in the schema to define output fields adds further clarity and organisation.

**Areas for Improvement:**

The email field is nullable in the database but requires validation in the schema. If it’s optional, consider conditionally validating only non-empty values. While the database enforces uniqueness, adding similar checks to the schema could prevent duplicate entries earlier in the process. For the join_date field, setting a default value (e.g., today’s date) could handle empty submissions better. Additionally, the rationale for using January 1, 2001, as the minimum date in validate_date_range is unclear; a comment could clarify this choice.

Lastly, refining the membership_number error message to emphasise its requirement for eight numeric characters could improve clarity.

***Action Taken:***
- Email changed to be not-null
- Code Comment addressing why January 1st 2001 is the minimum date for my validation
- Apostrophe's added to my validation in name

***Justification***
- The email field is critical for identifying and communicating with members, so making it non-null ensures the data's completeness and reliability. Previously, while the schema enforced validation on email format, the database allowed null values. This discrepancy could lead to inconsistent or incomplete data being stored. By setting email to NOT NULL, you ensure that both the schema and database align, preventing situations where invalid data bypasses validation and causing issues downstream.
- Including a code comment to explain why January 1st, 2001, was chosen as the minimum date improves code readability and maintainability. Without context, future developers (or even yourself) might question this arbitrary-looking constraint. Clarifying that it serves as a logical cutoff for "modern memberships" or aligns with system requirements removes ambiguity and enhances code transparency.
```January 1st, 2001 is used as the minimum join date to ensure no outdated or incorrect data is submitted.```
- Adding an apostrophe (') or refining validation for the name field clarifies the requirement to the user. Proper error messages improve usability by explicitly stating what input is acceptable. For example, ensuring names are alphabetic and meet other constraints (e.g., length or special character restrictions) helps users correct their input more efficiently. Improved error messages also make the system feel polished and user-friendly.

<br>

Who: Earvin\
When: 19/12/24\
What Document: error_handlers.py\
Feedback:
<br>
- Formatting the errors into functions does well to keep code DRY. Similar errors can just be called.
- Furthermore you have two types of Integrity errors in one function (unique and not null), and for unique violations put all the possible instances (name, email , ect) in an if/elif statement, this makes all the possible errors that can occur very clear and once again makes the code DRY
- Validation for your isbn is very thorough to make sure it is unique, has enough characters and hyphens.
- Code comments explain all errors and justifications for errors very clearly.

***Action Taken:***
No action needed as this is all positive feedback.

<br>

Who: Tanya\
When: 19/12/24\
What Document: Book.py\
Feedback:
<br>
Upon reviewing your book.py file for your Library Management System, I could not find any errors. My only suggestion and feedback would be to add docstrings to assist future developers understand the library terms a bit better, especially if they are not familiar with books or library systems. For example, for your book model class, you could include docstrings such as: 

        id (int): The unique identifier for the book.
        title (str): The title of the book.
        isbn (str): The International Standard Book Number (ISBN) of the book.
        available_copies (int): The number of copies currently available in the library.
        author_id (int): The ID of the author, referencing the authors table.
        genre_id (int): The ID of the genre, referencing the genres table.
        author (Author): The associated author object.
        genre (Genre): The associated genre object.
        loans (list): A list of loan records associated with the book. 

***Action Taken:***
- Docstrings added to Book.py to further explain the model.

***Justification:***
- The decision to add docstrings to the Book.py file was made to improve code readability and maintainability, especially for future developers who may be unfamiliar with the specific terms used in a library management system.

<br>

Who: Tilley\
When: 19/12/2024\
What Document: Loan.py\
Feedback:
<br>
Hey Evan I took a look at your code for loans model and schema.

Your code is well structured, the code comments are very detailed and the relationships between the tables are very clear and the unique constraint is implemented perfectly. well done!

Suggestions for improvement: 
if you have time maybe you can add validation for loan duration and maximum borrowing limits per member

***Action Taken:***
- Validation added for loan duration (30 Days) and maximum borrowing limits (5 books).
- I also added a return route and active/returned status for books.

***Justification:***
Adding these validations not only improves the fairness and reliability of the system but also prevents potential misuse and ensures smooth operations. It's a proactive step in managing resources effectively while offering an optimal experience for all users. Therefore, implementing these checks enhances both user satisfaction and system efficiency.

<br>

## Credits

Created by Evan Meehan.  
Contributions and guidance from Coder Academy educators.

