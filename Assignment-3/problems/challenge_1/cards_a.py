'''
Challenge 1
'''


def cards_game(m, n, k, counts):
    def can_stack(card1, card2):
        x_1, c_1 = card1
        x_2, c_2 = card2
        return (c_1 == c_2 and x_1 + 1 == x_2) or (x_1 == x_2 and c_1 != c_2)

    def dfs(player, cards):
        if not cards:
            return 0

        maxm_stacks = 0
        for card in cards:
            next_cards = [c for c in cards if can_stack(card, c)]
            stack_count = 1 + dfs((player % n) + 1, next_cards)
            maxm_stacks = max(maxm_stacks, stack_count)

        return maxm_stacks

    maxm_stacks = 0
    for player in range(1, n + 1):
        maxm_stacks = max(maxm_stacks, dfs(player, counts[player]))

    return maxm_stacks
