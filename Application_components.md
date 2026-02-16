Application Components of the Project
1️⃣ User Interface (Email Input Form)
Allows users to enter email subject and body

Acts as the interaction point for customers

Displays auto‑reply and detected category

2️⃣ Email Input Handler
Accepts email data from the user interface

Passes email content to the processing modules

Ensures required fields are present

3️⃣ Email Preprocessing Component
Converts text to lowercase

Removes unnecessary symbols and spaces

Prepares email text for classification

4️⃣ Email Classification Component
Analyzes email content

Matches keywords with predefined categories

Assigns a category such as:

Order Status

Refund / Payment

Account Issue

Complaint

General

5️⃣ Keyword Repository
Stores keywords for each email category

Used by the classification component

Can be updated by the administrator

6️⃣ Automated Response Generator
Selects a response template based on category

Generates an appropriate auto‑reply message

Ensures fast response without human involvement

7️⃣ Response Template Repository
Stores predefined reply messages

Maintains consistency in responses

Editable by the admin

8️⃣ Email Logging Component
Stores details of processed emails:

Sender

Subject

Category

Action taken

Helps in tracking and auditing

9️⃣ Admin Management Component
Allows admin to:

Update keywords

Update response templates

View email logs

Used for system maintenance

🔟 Support Executive Module
Handles emails that cannot be auto‑resolved

Manages forwarded or complex emails

Marks issues as resolved manually
