# program to shuffle the deck of cards declare card elements
suits = ["Spades", "Diamonds", "Club", "Heart"];
values = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King"
];

# Creating  empty array for storing cards

deck = [];

for i in range(0,len(suits)):
    for j in range(0,len(values)):
        class User():
            def __init__(self,values):
                self.Value=values
                self.Suit=suits[i]

        pair = User(values[j])
        deck.append(pair)

for i in range(0,len(deck)):
    
