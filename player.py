class Player:
    # All players have the same difficulty
    def __init__(self):
        self.__difficulty = self 

    def set_difficulty(self,  difficulty):
        self.__difficulty = difficulty

    def get_difficulty(self):

        return self.__difficulty


class Emil(Player):

    def __init__(self):
        super().__init__()
        self.__player_name = self

    def __str__(self):

        return str(self.get_player_name() + " " + self.get_highscore())

    def set_player_name(self):

        self.__player_name = "Emil"
    
    def get_player_name(self):

        return self.__player_name
    
    def set_highscore(self, highscore):
        f = open("stats\stats-emil.txt", "w")
        f.write(highscore)
        f.close()
        
    
    def get_highscore(self):
        f = open("stats\stats-emil.txt", "r")
        self.__highscore = f.read()
        return self.__highscore
    
class Iliyan(Player):

    def __init__(self):
        super().__init__()
        
        self.__player_name = self

    def __str__(self):

        return str(self.get_player_name() + " " + self.get_highscore())

    def set_player_name(self):

        self.__player_name = "Iliyan"
    
    def get_player_name(self):

        return self.__player_name
    
    def set_highscore(self, highscore):
        f = open("stats\stats-iliyan.txt", "w")
        f.write(highscore)
        f.close()
        
    
    def get_highscore(self):
        f = open("stats\stats-iliyan.txt", "r")
        self.__highscore = f.read()
        return self.__highscore






emil = Iliyan()
print(emil.get_highscore())
