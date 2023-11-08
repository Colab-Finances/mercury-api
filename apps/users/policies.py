from utils.auth.errors import ForbiddenError

class UserPolicy:

  def __init__(self, current_user) -> None:
    self.current_user = current_user

  def retrieve(self, resource_id):
    if self.current_user.id == resource_id:
      return 

    raise ForbiddenError