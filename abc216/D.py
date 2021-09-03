from collections import deque

N, M = map(int, input().split(" "))

tube = [deque() for i in range(M)]
on_ball = dict()
zero_t = 0
for i in range(M):
    print("-------")
    ki = int(input())
    for j in map(int, input().split(" ")):
        tube[i].append(j)
    color = tube[i].popleft()
    o_d = i
    colors = deque()

    while(color>=0):
        if color in on_ball:
            print("colors, on_ball {}, {}, {}".format(colors, on_ball, tube))
            o_d = on_ball[color] 
            del on_ball[color]

            if len(tube[o_d]) > 0:
                colors.append(tube[o_d].popleft())
                on_ball[color] = o_d
            else:
                zero_t +=1
        else:
            on_ball[color] = o_d

        
        if len(colors)>0:
            (color, o_d) = colors.popleft()
        else:
            color=-1
        
    
    if color != -1:
        on_ball[color] = o_d

    # print(zero_t)
    print("tube {}".format(tube))
    print("on_ball {}".format(on_ball))
