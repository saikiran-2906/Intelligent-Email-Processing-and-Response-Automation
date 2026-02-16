1️⃣ Presentation Layer (User Interface)
Component: Web Interface (HTML / CSS / JavaScript)

Description:
The Presentation Layer is the front-end of the system. It provides an interface through which users interact with the application.

Responsibilities:

Collects email subject and email body from the user

Sends the input data to the Flask controller

Displays:

Detected email category

Generated auto-reply message

Provides a clean and user-friendly experience

Technologies Used:

HTML – Structure of the page

CSS – Styling and layout

JavaScript – Client-side validation and interaction

Why this layer is important:
It separates user interaction logic from business logic, making UI changes easier without affecting backend functionality.

2️⃣ Application / Controller Layer
Component: Flask Controller

Description:
This layer acts as a bridge between the user interface and the business logic.

Responsibilities:

Receives HTTP requests from the Presentation Layer

Validates user input

Passes email data to the Business Logic Layer

Receives classification results and auto-reply

Sends processed results back to the UI

Key Role:

Controls the flow of execution

Ensures loose coupling between layers

Why this layer is important:
It centralizes request handling and avoids mixing UI code with processing logic.

3️⃣ Business Logic Layer

This is the core intelligence of the system.

🔹 Component 1: EmailClassifier

Description:
Responsible for understanding and classifying the email content.

Functions:

Preprocesses email text:

Converts text to lowercase

Removes punctuation and extra spaces

Uses keyword-based classification

Identifies categories such as:

Complaint

Inquiry

Feedback

Support request

Output:

Detected email category

🔹 Component 2: ResponseGenerator

Description:
Generates an appropriate auto-reply based on the classified category.

Functions:

Selects a predefined response template

Customizes the reply if required

Generates a professional response message

Output:

Auto-generated email reply

Why this layer is important:
It encapsulates all decision-making logic, making the system easy to enhance (e.g., adding ML models later).

4️⃣ Data Layer
Component: EmailLogger

Description:
Responsible for data storage and logging.

Responsibilities:

Stores:

Email subject

Email body

Detected category

Generated response

Date and time of processing

Maintains logs for:

Admin review

Support tracking

Optional Storage:

SQLite (for lab/demo)

MySQL (for scalable deployment)

Why this layer is important:
It ensures traceability, auditing, and debugging support.

5️⃣ Administrative Components

These components allow human control and system management.

🔹 Admin Module

Responsibilities:

Updates keyword lists for classification

Modifies auto-reply templates

Views processed email logs

Monitors system performance

Benefit:

Makes the system configurable without changing code

🔹 Support Executive Module

Responsibilities:

Handles emails that are:

Misclassified

Unresolved

Manually responds to complex issues

Updates resolution status

Benefit:

Ensures no important email is ignored

Provides human intervention when automation fails


