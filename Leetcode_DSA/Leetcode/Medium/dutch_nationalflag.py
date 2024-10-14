def dutch_flag(balls):

    p0 = 0
    curr = 0
    p2 = len(balls)-1
    while curr <= p2:
        if balls[curr] == 2:
            balls[curr],balls[p2] = balls[p2],balls[curr]
            p2 -= 1
            curr += 1
        elif balls[curr] == 0:
            balls[curr], balls[p0] = balls[p0], balls[curr]
            p0 += 1
            curr += 1
        else:
            curr += 1




    return balls

print(dutch_flag([2,0,2,1,1,0]))

