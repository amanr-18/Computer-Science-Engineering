# cook your dish here

def knapsack(dp, cnt_red, red, blue):

    

    def recur(ind, red_wanted):

        nonlocal dp

        

        if (ind, red_wanted) in dp:

            return dp[(ind, red_wanted)]

            

        if ind == len(red):

            if red_wanted>0:

                dp[(ind, red_wanted)] = -float('inf')

            else:

                dp[(ind, red_wanted)] = 0

                

        else:

            if red_wanted <= 0:

                s = 0

                

                for i in range(ind, len(red)):

                    s+=blue[i]

                    

                dp[(ind, red_wanted)] = s

                

            else:

                dp[(ind, red_wanted)] = max(recur(ind+1, red_wanted - red[ind]), recur(ind+1, red_wanted) + blue[ind])

                

        return dp[(ind, red_wanted)]

            

    blue_cnt = recur(0, cnt_red)

    

    return blue_cnt

    

for t in range(int(input())):

    n = int(input())

    red = [int(x) for x in input().split(" ")]

    blue = [int(x) for x in input().split(" ")]

    

    high = sum(red)

    low = 0

    

    dp = {}

    maxx = 0

    

    #dp stores - 

    #for particular no of red flowers, how many max no of blue flowers can i get

    

    while low<=high:

        

        mid = (low+high)//2

        

        temp_b = knapsack(dp, mid, red, blue)

        

        if temp_b<mid:

            high = mid-1

        elif temp_b>mid:

            low = mid+1

        else:

            maxx = max(maxx, temp_b)

            break

        

        maxx = max(maxx, min(temp_b, mid))

        

    print(maxx)

    

        

    

    

