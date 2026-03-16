classifier = EmailClassifier()
responder = ResponseGenerator()

email = input("Enter email text: ")

category = classifier.classify(email)
response = responder.generate_response(category)

print("Detected Category:", category)
print("Auto Response:", response)
