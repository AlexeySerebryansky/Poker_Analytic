class GameStateError(Exception):

     def __init__(self, user_massage: str):
         self.user_massage = user_massage
         super().__init__(user_massage)