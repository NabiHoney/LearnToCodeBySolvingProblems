deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
complete_deck = deck * 4

n = int(input())

counted = 0

for i in range(n):
    cards_drawn=int(input())
    counted = counted + cards_drawn
    complete_deck.remove(cards_drawn)

diff = 21 - counted
more = 0

for i in (complete_deck):
    if i>diff:
        more = more + 1

if more > 52 - n - more:
    print('DOSTA')
else:
    print('VUCI')
