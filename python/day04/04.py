from pathlib import Path


class Card():
    card_number = None
    _solved = False
    _points = 0
    matched_numbers = 0
    winn_copies = list()

    @property
    def points(self):
        if not self._solved:
            self.solve()
        return self._points

    def __init__(self, line) -> None:
        winning_numbers, just_numbers = line.split('|')
        card_number = winning_numbers.split(':')[0].split(' ')
        card_number = [n.strip() for n in card_number if n]
        self.card_number = int(card_number[1])
        winning_numbers = winning_numbers.split(':')[1].split(' ')
        self.winning_numbers = [int(n.strip()) for n in winning_numbers if n]
        
        just_numbers = just_numbers.split(' ')
        self.just_numbers = [int(n.strip()) for n in just_numbers if n]
    
    def solve(self):
        if not self._solved:
            for wn in self.winning_numbers:
                if wn in self.just_numbers:
                    self.matched_numbers += 1
            if self.matched_numbers > 0:
                self._points = pow(2, self.matched_numbers-1)    
            self._solved = True


# input = Path('input.txt').read_text().splitlines()
input = Path('puzzle_input.txt').read_text().splitlines()


cards = [Card(line) for line in input]

# part1
card_points = [card.points for card in cards]
print(sum(card_points))


# part2
def get_cards_numbers(test_cards):
    return [c.card_number for c in test_cards]


def explore_cards(cards_origin, test_cards):
    local_sum = 0
    if len(test_cards) == 0:
        return 0
    
    for card in test_cards:
        # see what cards it wins
        card_index = card.card_number - 1
        tmp_cards = list()
        for i in range(card_index + 1, card_index + 1 + card.matched_numbers):
            tmp_cards.append(cards_origin[i])
        local_sum += explore_cards(cards_origin, tmp_cards) + len(tmp_cards)
    return local_sum


total_sum = explore_cards(cards_origin=cards, test_cards=cards) + len(cards)
print(total_sum)