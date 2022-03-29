class Player:

    def __init__(self, highscore, NOG):
        self.__highscore = highscore
        self.number_of_games = NOG

    def set_highscore(self, highscore):
        self. __highscore = highscore
    
    def get_highscore(self):
        return self.__highscore
    
    def set_number_of_games(self, NOG):
        self.number_of_games = NOG

    def get_number_of_games(self):

        return self.number_of_games

class Emil(Player):

    def __init__(self, highscore, NOG, player_name):
        super().__init__(highscore, NOG)
        self.__player_name = player_name

    def __str__(self):

        return str(str(self.get_highscore()) + str(self.get_number_of_games()) + self.get_player_name())

    def set_player_name(self, player_name):

        self.__player_name = player_name
    
    def get_player_name(self):

        return self.__player_name






emil = Emil(12, 3, "Emil")
print(emil)
