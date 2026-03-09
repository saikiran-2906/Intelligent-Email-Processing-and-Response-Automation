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

        return self.logs