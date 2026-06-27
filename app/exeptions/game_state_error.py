class GameStateError(Exception):

    def __init__(self, user_message:str):

        self.user_message = user_message
        super().__init__(self.user_message)