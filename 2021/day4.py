class Number:
    def __init__(self, n):
        self.n = n
        self.marked = False

    def __eq__(self, b):
        return self.n == b


class BingoCard:
    def __init__(self, card):
        """5x5 bingo card"""
        self.card = card
        self.n = -1
        self.winner = False
        for x in range(5):
            for y in range(5):
                self.card[x][y] = Number(self.card[x][y])

    def mark(self, n):
        # don't mark an already won bingo card
        if self.winner:
            return

        for x in range(5):
            for y in range(5):
                if self.card[x][y] == n:
                    self.card[x][y].marked = True
                    self.n = n

        if self._check_bingo():
            self.winner = True

    def _check_bingo(self) -> bool:
        row = [False for _ in range(5)]
        for x in range(5):
            for y in range(5):
                row[y] = self.card[x][y].marked

            if False not in row:
                return True

            row = [False for _ in range(5)]

        col = [False for _ in range(5)]
        for y in range(5):
            for x in range(5):
                col[x] = self.card[x][y].marked

            if False not in col:
                return True

            col = [False for _ in range(5)]

        return False

    @property
    def score(self) -> int:
        """Sum unmarked numbers, multiply by last number called"""
        total = 0
        for x in range(5):
            for y in range(5):
                if not self.card[x][y].marked:
                    total += self.card[x][y].n

        return total * self.n


def part1(bingo_cards, numbers):
    for n in numbers:
        for c in bingo_cards:
            c.mark(n)
            if c.winner:
                return c.score


def part2(bingo_cards, numbers):
    winners = []
    for n in numbers:
        for c in bingo_cards:
            c.mark(n)
            if c.winner and c.score not in winners:
                winners.append(c.score)

    return winners[-1]


def main():
    with open("day4.input") as f:
        numbers = list(map(int, f.readline().split(",")))
        f.readline()
        card = []
        bingo_cards = []
        for line in f:
            if line == "\n":
                bingo_cards.append(BingoCard(card))
                card = []
            else:
                card.append([int(n.strip()) for n in line.split(" ") if n.strip()])
        bingo_cards.append(BingoCard(card))

    print(part1(bingo_cards, numbers))
    print(part2(bingo_cards, numbers))


if __name__ == "__main__":
    main()
