import random


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"{self.name}: {self.hand}"

    def get(self):
        if self.hand:
            return self.hand.pop(0)
        print(f"{self.name} nie ma już kart do gry!")
        exit(0)

    def set(self, card):
        return self.hand.extend(card)


class Game:

    def __init__(self):
        self.players = [Player("Gracz 1"), Player("Gracz 2")]
        self._actual_player = 0
        self.hand1 = []
        self.hand2 = []
        self.round_no = 0

    def deal(self):
        """
        Rozdanie kart. Program tworzy talię, tasuje ją, po czym rozdaje na
        przemian obu graczom.

        Talia kart: wartości od 2 do 14 – by uprościć porównania zastąpiono
        figury J, Q, K, A odpowiadającymi im kolejnymi wartościami:
        11, 12, 13, 14. W grze w wojnę kolory kart (pik, trefl, karo i kier) są
        nieistotne, zatem w symulacji zrezygnowano z nich, tworząc po prostu
        cztery kopie każdej karty.
        """

        # przygotowanie talii
        deck = [card for card in range(2, 15) for _ in range(4)]

        # tasowanie
        random.shuffle(deck)

        # rozdanie
        while deck:
            card = deck.pop()
            self.players[self._actual_player].hand.append(card)
            self._actual_player = 1 - self._actual_player

    def play(self):

        h1 = self.players[0].get()
        h2 = self.players[1].get()

        self.hand1.append(h1)
        self.hand2.append(h2)

        print(f"Na stole:  1. {self.hand1}, 2. {self.hand2}")

        if h1 > h2:
            self.players[0].set(self.hand1)
            self.players[0].set(self.hand2)
            print(f"Wygrał {self.players[0].name}\n")
        elif h2 > h1:
            self.players[1].set(self.hand1)
            self.players[1].set(self.hand2)
            print(f"Wygrał {self.players[1].name}\n")
        else:
            # wojna!
            # pobieramy jedną kartę zakrytą
            h1 = self.players[0].get()
            h2 = self.players[1].get()

            self.hand1.append(h1)
            self.hand2.append(h2)

            print("WOJNA!")
            # ...i jeszcze raz wywołujemy rundę
            self.play()

        # czyścimy rękę
        self.hand1 = []
        self.hand2 = []


def go():
    g = Game()
    g.deal()

    while g.players[0].hand and g.players[1].hand:
        print(f"RUNDA {g.round_no}.")
        print(f"{g.players[0]}")
        print(f"{g.players[1]}")
        g.play()
        g.round_no += 1
        if g.round_no % 10 == 0:
            print("tasowanie")
            random.shuffle(g.players[0].hand)
            random.shuffle(g.players[1].hand)

    winner = g.players[1] if not g.players[0].hand else g.players[0]
    print(f"\nZwycięzca: {winner.name}")


if __name__ == "__main__":
    go()
