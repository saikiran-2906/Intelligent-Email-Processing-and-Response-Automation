## Core Functional Modules in Business Logic Layer 

The **Business Logic Layer (BLL)** is responsible for implementing the core functionality and decision-making logic of the system. In the **Intelligent Email Processing and Response Automation System**, the following modules are included:

---

### 1️. Email Classification Module

**Description:**  
This module analyzes incoming emails and assigns them to appropriate categories such as:
- Order Query  
- Refund Request  
- Complaint  
- Account Issue  

**Logic:**  
Classification is performed using keyword-based matching or machine learning techniques.

**Example:**
- Email containing "refund" → categorized as Refund Request  

**Interaction with UI:**
- User submits email through the frontend  
- UI sends data to backend  
- Classification result is returned and displayed  

---

### 2️. Response Generation Module

**Description:**  
Generates automated replies based on the classified category.

**Logic:**  
Each category has a predefined response template.

**Example:**
- Refund Request → "Your refund request has been received and is being processed."

**Purpose:**
- Reduces manual effort  
- Ensures quick response to users  

**Interaction with UI:**
- Generated response is sent back after classification  
- UI displays the response  

---

### 3️. User Authentication Module

**Description:**  
Verifies user credentials and provides role-based access.

**Roles Include:**
- Customer  
- Admin  
- Support Executive  

**Functionality:**
- Validates username and password  
- Redirects users to respective dashboards  

**Interaction with UI:**
- Login form sends credentials  
- BLL validates them  
- User is redirected to correct dashboard  

---

### 4️. Email Logging Module

**Description:**  
Stores processed email details for monitoring and analysis.

**Data Stored:**
- Sender  
- Subject  
- Category  
- Response  

**Purpose:**
- Helps admin track system activity  
- Maintains history of emails  

**Interaction with UI:**
- Admin dashboard fetches logs  
- Displays them to user  

---

### 5️. Manual Response Module (Support System)

**Description:**  
Handles emails that cannot be classified automatically.

**Functionality:**
- Displays unresolved emails  
- Allows support staff to send manual replies  

**Interaction with UI:**
- Support dashboard shows pending emails  
- Allows manual response submission  


