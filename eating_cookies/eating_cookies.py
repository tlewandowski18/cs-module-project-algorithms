'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # Your code here
#     if n == 0 or n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache={}):
    if n == 0:
        cache[0] = 1
        return 1
    if n == 1:
        cache[1] = 1
        return 1
    if n == 2:
        cache[2] = 2
        return 2
    if n in cache:
        return cache[n]
    
    result_n_1 = eating_cookies(n-1, cache)
    result_n_2 = eating_cookies(n-2, cache)
    result_n_3 = eating_cookies(n-3, cache)
    result_n = result_n_1 + result_n_2 + result_n_3

    cache[n] = result_n

    return result_n

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 6

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
