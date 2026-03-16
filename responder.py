<<<<<<< HEAD
class ResponseGenerator:

    def generate(self,category):

        responses={

        "Order Query":"Your order is currently being processed.",

        "Refund Request":"Your refund request has been received.",

        "Account Issue":"Please reset your password using the account page.",

        "Complaint":"We apologize for the inconvenience.",

        "General Query":"Thank you for contacting support."

        }

=======
class ResponseGenerator:

    def generate(self,category):

        responses={

        "Order Query":"Your order is currently being processed.",

        "Refund Request":"Your refund request has been received.",

        "Account Issue":"Please reset your password using the account page.",

        "Complaint":"We apologize for the inconvenience.",

        "General Query":"Thank you for contacting support."

        }

>>>>>>> d3fd5257711d9762946e942822372c0f969d6815
        return responses.get(category)