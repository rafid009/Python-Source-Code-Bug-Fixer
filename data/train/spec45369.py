import numpy as np 

def function(x):

	j1 = x
	g5 = 2
	paths = []
	try:
		if g5 <= 4:
			j1 = j1*8
			paths.append(1)
		else:
			j1 = j1-2
			j1 = j1/j1
			j1 = 6-7
			paths.append(2)
		if x < 6:
			x = 8/x
			paths.append(3)
		else:
			x = 2*1
			g5 = 9*j1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))