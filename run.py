from app.models import User
from app.data.data import inputs

user = User(inputs)
print(user.get_inputs())
