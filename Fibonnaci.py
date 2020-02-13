import time
import matplotlib.pyplot as plt
import numpy as np

def recur_fib1(n):
	if n < 0:
		print("Incorrect input")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return(recur_fib1(n-1) + recur_fib1(n-2))

def iter_fib2(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a

FibArray = [0,1] 
  
def dynamic_fib3(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = dynamic_fib3(n-1)+dynamic_fib3(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 

fib1Time = []
fib2Time = []
fib3Time = []
graphLimit = []

def test_run():
	n = int(input("What number of the sequence are you looking for?: "))
	graphLimit.append(n)

	print("for recursion:")
	fib1Start = time.time()
	print(recur_fib1(n))
	fib1End = time.time()
	fib1Result = fib1End - fib1Start
	print("Time elapsed for recursion: ", round(fib1Result), "secs\n")
	fib1Time.append(fib1Result)

	print("for iteration:")
	fib2Start = time.time()
	print(iter_fib2(n))
	fib2End = time.time()
	fib2Result = fib2End - fib2Start
	print("Time elapsed for iteration: ", round(fib2Result), "secs\n")
	fib2Time.append(fib2Result)

	print("for dynamic:")
	fib3Start = time.time()
	print(dynamic_fib3(n))
	fib3End = time.time()
	fib3Result = fib3End - fib3Start
	print("Time elapsed for dynamic: ", round(fib3Result), "secs\n")
	fib3Time.append(fib3Result)

	Q = input("would you like to run another test? (y/n): ")
	if Q == "y":
		test_run()
	else:
		print("results of your tests are in order: \n")

test_run()
print("please wait for the graph......")

fig, (ax1,ax2,ax3) = plt.subplots(3)
fig.suptitle("Results of the tests")
ax1.plot(fib1Time,graphLimit,'g')
ax1.set_ylabel("recursion")

ax2.plot(fib2Time,graphLimit,'r')
ax2.set_ylabel("iteration")

ax3.plot(fib3Time,graphLimit,'y')
ax3.set_ylabel("dynamic")
ax3.set_xlabel("Time")
plt.show()
