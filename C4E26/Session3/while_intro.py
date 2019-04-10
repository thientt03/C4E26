loop_count = 0
loop = True
while True:
    print("Running...")
    loop_count += 1
    print(loop_count)
    if loop_count > 2:
        loop = False