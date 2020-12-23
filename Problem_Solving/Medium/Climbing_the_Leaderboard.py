def climbingLeaderboard(scores, alice):
    arr = [1 for i in range(len(alice))]
    scores_rank = list(set(scores))
    scores_rank.sort()
    scores_rank.reverse()
    for i in alice:
        rank = 1
        for j in scores_rank:
            if i >= j:
                break
            else:
                rank += 1
        print(rank)
    print(arr)


scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
climbingLeaderboard(scores, alice)