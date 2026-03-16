#####Email Classifier

class EmailClassifier:

    def __init__(self):
        self.keyword_dict = {
            "Order": ["order", "delivery", "shipment", "tracking"],
            "Refund": ["refund", "payment", "charged", "money"],
            "Account": ["password", "login", "account", "reset"], 
            "Complaint": ["complaint", "issue", "problem", "error"]
        }

    def preprocess(self, text):
        text = text.lower()
        return text

    def classify(self, email_text):
        text = self.preprocess(email_text)

        scores = {}
        for category, keywords in self.keyword_dict.items():
            scores[category] = 0
            for word in keywords:
                if word in text:
                    scores[category] += 1

        best_category = max(scores, key=scores.get)

        if scores[best_category] == 0:
            return "General"
        return best_category
