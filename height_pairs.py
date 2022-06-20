# Import needed modules
import requests as req

# url where the data is provided
url = 'https://mach-eight.uc.r.appspot.com/'

# use http get to obtain the data as json
resp = req.get(url).json()
data = resp.items()

# transform data into a list of tuples
players = []
for key, value in data:
    for k in range(len(value)):
        players.append((value[k]['first_name'] + ' ' + value[k]['last_name'], int(value[k]['h_in'])))

# collect and sort the players heights
heights = []
for k in range(len(players)):
    if players[k][1] not in heights:
        heights.append(players[k][1])

sorted_heights = sorted(heights)

# define binary search for faster performance
def find_index(elements, value):
    left, right = 0, len(elements) - 1
    
    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            return middle

        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1

# define function to select the wanted pairs given an integer h
def find_macthing_pairs(h):
    '''This function find all pairs of players whose heights add up to h'''
    try:
        pairs = []
        for k in range(len(players)):  
            # item to search in the sorted list of heights
            target = h - players[k][1]

            # find the index of target using binary search
            idx = find_index(sorted_heights, target)
            if isinstance(idx, int) and idx > -1:

            # find and append every pair of players whose heights add up to h
                for l in range(k + 1, len(players)):
                    pair = (players[k][0] + ' '*10 +  players[l][0])
                    if players[l][1] == sorted_heights[idx] and pair not in pairs:
                        pairs.append(pair)

        # when there are no matching pairs
        if len(pairs) == 0:
            return "No matches found!"

        # when there are matching pairs
        else:
            return [print(p) for p in pairs]

    # in case that h is not an integer
    except:
        print('h is invalid.')


find_macthing_pairs(139)