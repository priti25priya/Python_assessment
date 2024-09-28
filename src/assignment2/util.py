def find_runner_up_score():

    n = int(input("Enter the number of participants: "))
    number = input(f"Enter the {n} scores separated by spaces or commas: ")
    scores = list(map(int, number.replace(',', ' ').split()))
    unique_scores = set(scores)
    unique_scores.remove(max(unique_scores))
    runner_up_score = max(unique_scores)

    return runner_up_score


