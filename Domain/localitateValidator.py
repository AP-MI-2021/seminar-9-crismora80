from Domain.localitate import Localitate


class LocalitateValidator:
    def valideaza(self, localitate: Localitate):
        erori = []
        if localitate.nume == "":
            erori.append("Numele localitatii nu poate fi gol!")
        if localitate.tip not in ["sat", "oras", "municipiu"]:
            erori.append("Tipul localitatii poate fi doar sat/oras/municipiu!")
        if erori:
            raise ValueError(erori)