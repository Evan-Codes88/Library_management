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
  - [How to Run the API](#how-to-run-the-api)
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
    Replace username, password, and localhost with your postgreSQL credentials.

### **Initialize the Database Tables**

Use Flask CLI commands to create the necessary tables:

```bash
flask db create # This creates your entity tables
flask db seed # This seeds alll of the data
flask db drop # This will drop all tables and relations
```

### How to Run the API

1. Ensure your virtual environment is activated.
2. Start the API server:
   ```bash
   flask run
   ```
3. Access the API at `http://localhost:5432`.

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
- ' added to my validation in name

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

## Credits

Created by Evan Meehan.  
Contributions and guidance from Coder Academy educators.

