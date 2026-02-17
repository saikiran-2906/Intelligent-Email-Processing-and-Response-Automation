I‑A. Justification of Architecture Style
(Layered Architecture with Examples)

✅ What granularity means (with example)
->Granularity = how software is broken into small focused parts
->Each part does only one job

👉 Example in our project:

->  EmailClassifier → only classifies emails
-> ResponseGenerator → only generates replies
-> EmailLogger → only stores records
-> Each component has one responsibility.

---------------------------------------------------------

✅ Component separation (real example)
Our system does NOT mix tasks.
Instead of one big program doing everything:

-> each task is separated

Example flow:
  User email → Classifier → ResponseGenerator → Logger


-> Classifier doesn’t send replies
-> Logger doesn’t classify emails
-> ResponseGenerator doesn’t store logs
👉 This shows clean granularity

-----------------------------------------------------------
✅ Independence of components (example)
If we change one part, others still work.

Example 1:
-> You upgrade classifier from keyword rules → AI model
-> UI and Logger remain unchanged

Example 2:
-> You change response templates
->Classification logic stays same
👉 Components are independent

-------------------------------------------------------------

✅ Replaceability example
Any component can be replaced without breaking system.
Example:

->Replace web UI with mobile app
->Backend classifier still works
👉 This proves layered granularity

-------------------------------------------------------------------

✅ Cohesion inside each component
Each module is focused.

Example:

EmailLogger only:
->logEmail()
->viewLogs()

It does not classify or reply.

👉 High cohesion = good design

-------------------------------------------------------------------

✅ Low coupling between components
Modules communicate through inputs and outputs only

Classifier → sends category
ResponseGenerator → receives category

They don’t access each other’s internal data.

👉 Low coupling = easier maintenance

