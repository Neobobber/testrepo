

with open("f:\python/hocus/analogieshard.txt", "r") as input:
    with open("newfile.txt", "w") as output:
        for line in input:
            if line.strip("\n") != '<div class="testsoverzicht">':
                output.write(line)
                print("r1done")
        for line in input:
            if line.strip("\n") != '<h2>Start the Test!</h2>':
                output.write(line)
                print("r2done")
        for line in input:
            if line.strip("\n") != '<div class="embedcode">':
                output.write(line)
                print("r3done")




root.mainloop()