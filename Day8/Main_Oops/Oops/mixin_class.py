class LogMixin:
    def log(self, message):
        print(f'Log: {message}')
        
class User(LogMixin):
    
    def create_user(self, name):
        self.log(f'User {name} created.')
    
user = User()
user.create_user('Sankar')