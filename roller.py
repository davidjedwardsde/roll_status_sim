import random as rand
import matplotlib.pyplot as plt


def roll(x):  # base logic for single dice roller
    results = []
    for i in range(x):
        dice = rand.randint(1, 20)
        results.append(dice)
    return results


def roll_advantage(x):
    results_adv = []
    for i in range(x):
        dice_1 = rand.randint(1, 20)
        dice_2 = rand.randint(1, 20)
        if dice_1 > dice_2:
            results_adv.append(dice_1)
        else:
            results_adv.append(dice_2)
    return results_adv


def roll_disadvantage(x):
    results_dis = []
    for i in range(x):
        dice_1 = rand.randint(1, 20)
        dice_2 = rand.randint(1, 20)
        if dice_1 > dice_2:
            results_dis.append(dice_2)
        else:
            results_dis.append(dice_1)
    return results_dis


def roll_sim(trials, rolls):  # base simulation logic
    data_standard = []
    data_advantage = []
    data_disadvantage = []
    for i in range(trials):
        trial_standard = roll(rolls)
        avg_standard = sum(trial_standard) / len(trial_standard)
        data_standard.append(avg_standard)

        trial_advantage = roll_advantage(rolls)
        avg_advantage = sum(trial_advantage) / len(trial_advantage)
        data_advantage.append(avg_advantage)

        trial_disadvantage = roll_disadvantage(rolls)
        avg_disadvantage = sum(trial_disadvantage) / len(trial_disadvantage)
        data_disadvantage.append(avg_disadvantage)

    plt.figure(figsize=(8, 6))
    plt.hist(data_standard, alpha=0.5, label="Standard Roll")
    plt.hist(data_advantage, alpha=0.5, label="Advantage Roll")
    plt.hist(data_disadvantage, alpha=0.5, label="Disadvantage Roll")
    plt.suptitle("Effects of Advantage and Disadvantage on D20 Dice Roll")
    plt.title(f"Result of averaging {rolls:,} rolls {trials:,} times")
    plt.xlabel("Avg Dice Score")
    plt.ylabel("Frequency of Score")
    plt.legend(loc='upper right')
    plt.show()


test = roll_sim(10000, 100)

