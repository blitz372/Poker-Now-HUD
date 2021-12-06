import re

log_name = "C:/Users/JMays/Documents/code/Poker-Now-HUD/Poker Log Big Week.csv"

hand_end_re = re.compile(r'"-- ending hand #\d+ --"')
hand_start_re = re.compile(
    r'"-- starting hand #\d+  \(No Limit Texas Hold\'em\) \(dealer: ""(.+) @ (.+)""\) --"')
hands = []

with open(log_name, 'r') as log:
    for line in log:
        action = line.split(',', 1)[0]
        match = hand_end_re.match(action)
        if match:
            actions = []
            actions.append(action)
            for line in log:

                action = line.split(',', 1)[0]
                match = hand_start_re.match(action)
                actions.append(action)
                if match:
                    hands.append(actions)
                    break
