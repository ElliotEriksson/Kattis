from collections import Counter
hand = input().split()
deck = []
for card in hand:
    deck.append(card[:1])
counts = (Counter(deck))
print(max(counts.values()))