from random import randint as rand
import statistics as stat

R = 50000
ns = [20, 50, 150]
N = 150

def nr1(n):
    res = []
    for r in range(R):
        nums = []
        for _ in range(n):
            nums.append(rand(1, N))
        r = max(nums)
        res.append(r)
    return res

def nr2(n):
    res = []
    for r in range(R):
        nums = []
        for _ in range(n):
            nums.append(rand(1, N))
        r = 2 * (sum(nums)/len(nums)) - 1
        res.append(r)
    return res

def nr3(n):
    res = []
    for r in range(R):
        nums = []
        for _ in range(n):
            nums.append(rand(1, N))
        r = ((n + 1)/n) * max(nums)
        res.append(r)
    return res

if __name__ == "__main__":
    for n in ns:
        res_1 = nr1(N)
        res_2 = nr2(N)
        res_3 = nr3(N)

        print(f'N: {n}, Nr 1 mean: {stat.mean(res_1)}, Nr 1 std: {stat.stdev(res_1)}, Nr 2 mean: {stat.mean(res_2)}, Nr 2 std: {stat.stdev(res_2)}, Nr 3 mean: {stat.mean(res_3)}, Nr 3 std: {stat.stdev(res_2)}')



