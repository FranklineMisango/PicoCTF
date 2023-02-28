import random
import os

FLAG_BUFFER = 128
MAX_SYM_LEN = 4


class Stonk:
    def __init__(self):
        self.shares = None
        self.symbol = None
        self.next = None


class Portfolio:
    def __init__(self):
        self.money = None
        self.head = None


def view_portfolio(p):
    if not p:
        return 1
    print(f"\nPortfolio as of {os.popen('date').read().strip()}\n\n")
    head = p.head
    if not head:
        print("You don't own any stonks!\n")
    while head:
        print(f"{head.shares} shares of {head.symbol}\n")
        head = head.next
    return 0


def pick_symbol_with_AI(shares):
    if shares < 1:
        return None
    stonk = Stonk()
    stonk.shares = shares

    AI_symbol_len = random.randint(1, MAX_SYM_LEN)
    stonk.symbol = ''.join(['A' + chr(random.randint(0, 25))])
