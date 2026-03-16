<<<<<<< HEAD
class EmailLogger:

    def __init__(self):

        self.logs=[]

    def log_email(self,sender,subject,category):

        log={

        "sender":sender,

        "subject":subject,

        "category":category

        }

        self.logs.append(log)

    def view_logs(self):

=======
class EmailLogger:

    def __init__(self):

        self.logs=[]

    def log_email(self,sender,subject,category):

        log={

        "sender":sender,

        "subject":subject,

        "category":category

        }

        self.logs.append(log)

    def view_logs(self):

>>>>>>> d3fd5257711d9762946e942822372c0f969d6815
        return self.logs