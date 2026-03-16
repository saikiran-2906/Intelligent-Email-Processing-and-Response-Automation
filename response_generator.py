class ResponseGenerator:

    def __init__(self):
        self.templates = {
            "Order": "Your order is being processed. Thank you for your patience.",
            "Refund": "Your refund request has been received. We will update you shortly.",
            "Account": "Please use the password reset link to recover your account.",
            "Complaint": "We are sorry for the inconvenience. Our team will contact you.",
            "General": "Thank you for contacting support. We will respond soon."
        }

    def generate_response(self, category):
        return self.templates.get(category, self.templates["General"])
