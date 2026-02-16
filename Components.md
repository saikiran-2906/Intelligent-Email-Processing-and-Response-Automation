 Components (Application Components) 
The system is divided into the following layers and components:

1️⃣ Presentation Layer (User Interface)
Web Interface (HTML/CSS/JS)

Collects email subject and body

Displays detected category and auto‑reply

2️⃣ Application / Controller Layer
Flask Controller

Receives user requests

Coordinates flow between layers
3️⃣ Business Logic Layer
Core intelligence of the system:

EmailClassifier

Preprocesses email text

Classifies email using keywords

ResponseGenerator

Selects appropriate auto‑reply

Generates response message

4️⃣ Data Layer
EmailLogger

Stores processed email details

Maintains logs for admin and support

(Optional: Database such as SQLite / MySQL)

5️⃣ Administrative Components
Admin Module

Updates keywords

Updates response templates

Views email logs

SupportExecutive Module

Handles unresolved emails

Manually resolves issues
