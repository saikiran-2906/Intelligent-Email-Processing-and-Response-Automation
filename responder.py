class ResponseGenerator:

    def generate(self,category):

        responses={

        "Order Query":"Your order is currently being processed.",

        "Refund Request":"Your refund request has been received.",

        "Account Issue":"Please reset your password using the account page.",

        "Complaint":"We apologize for the inconvenience.",

        "General Query":"Thank you for contacting support."

        }

        return responses.get(category)