class EmailClassifier:

    def __init__(self):

        self.keywords = {

        "Order Query":["order","delivery","shipment"],

        "Refund Request":["refund","return","money"],

        "Account Issue":["password","login","account"],

        "Complaint":["problem","issue","error"]

        }

    def classify(self,text):

        text=text.lower()

        for category,words in self.keywords.items():

            for w in words:

                if w in text:

                    return category

        return "General Query"