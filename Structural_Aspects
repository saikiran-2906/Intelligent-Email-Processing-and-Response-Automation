🔷 Q1. Key Classes, Attributes & Methods
1️⃣ Class: Email
Purpose: Represents an incoming customer email.

Attributes
- emailId : int

- sender : String

- subject : String

- body : String

- category : String

- status : String

Methods
+ getContent() : String

+ setCategory(String) : void

+ getCategory() : String

+ markProcessed() : void

2️⃣ Class: EmailClassifier
Purpose: Classifies emails into categories.

Attributes
- keywordDictionary : Map

Methods
+ preprocess(text:String) : String

+ classify(email:Email) : String

+ matchKeywords(text:String) : String

3️⃣ Class: ResponseGenerator
Purpose: Generates automated replies.

Attributes
- templates : Map

Methods
+ generateResponse(category:String) : String

+ sendResponse(email:Email) : void

4️⃣ Class: EmailLogger
Purpose: Stores email history.

Attributes
- logDatabase : List

Methods
+ logEmail(email:Email) : void

+ viewLogs() : List

5️⃣ Class: Admin
Purpose: Maintains system configuration.

Attributes
- adminId : int

- name : String

Methods
+ updateKeywords() : void

+ updateTemplates() : void

+ viewLogs() : void

6️⃣ Class: SupportExecutive
Purpose: Handles forwarded emails.

Attributes
- employeeId : int

- name : String

Methods
+ handleEmail(email:Email) : void

+ resolveIssue() : void
