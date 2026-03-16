# Use Case Diagram Explanation

## Intelligent Email Processing and Response Automation System (E-commerce)

This document explains the use case diagram for the **Intelligent Email Processing and Response Automation System**, designed to handle customer emails efficiently in an e-commerce environment.

---

## 1. System Boundary

The system boundary is represented by a rectangle labeled:

**“Intelligent Email Processing and Response Automation System”**

* All functionalities inside the rectangle are performed by the software system.
* All entities outside the rectangle are external users (actors) interacting with the system.

---

## 2. Actors (External Users)

### 1. Customer

**Role:** End user of the e-commerce platform.

**Responsibilities:**

* Sends emails related to orders, refunds, complaints, or general queries.
* Receives automated responses from the system.

**Associated Use Cases:**

* Submit Customer Email
* Send Automated Reply

---

### 2. Support Executive

**Role:** Human support staff handling cases that require manual attention.

**Responsibilities:**

* Manages emails that cannot be fully resolved by automation.
* Reviews previous email interactions for context.

**Associated Use Cases:**

* Forward Email to Department
* View Email Logs

---

### 3. Admin

**Role:** System administrator responsible for configuration and monitoring.

**Responsibilities:**

* Maintains classification rules and response templates.
* Monitors system activity and email processing logs.

**Associated Use Cases:**

* View Email Logs
* Manage Keywords & Templates

---

## 3. Use Cases (System Functionalities)

### Submit Customer Email

* The customer sends an email to the system.
* This acts as the entry point of the entire workflow.

---

### Preprocess Email Content

* The system cleans and standardizes the email content.
* Examples include converting text to lowercase and removing unnecessary symbols.

---

### Classify Email

* The system identifies the intent of the email.
* Common categories include:

  * Order Status
  * Refund
  * Complaint
  * General Query

---

### Generate Automated Response

* Based on the classified category, the system prepares a suitable response using predefined templates.

---

### Send Automated Reply

* The generated response is sent back to the customer automatically.

---

### Forward Email to Department

* If the system determines that automation is insufficient, the email is forwarded to the appropriate support executive or department.

---

### Log Email Details

* The system records important information such as:

  * Email content
  * Classified category
  * Action taken
  * Timestamp

---

### View Email Logs

* Support Executives and Admins can access logs to review processed emails.

---

### Manage Keywords & Templates

* The Admin updates:

  * Keyword lists used for email classification
  * Response templates used for automated replies

---

This use case diagram clearly shows how customer emails flow through the system from submission to resolution, ensuring efficiency, scalability, and reduced manual workload.
