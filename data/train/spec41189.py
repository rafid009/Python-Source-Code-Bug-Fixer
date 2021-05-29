import numpy as np 

def function(x):

	j1 = 3
	y7 = 6
	paths = []
	try:
		if x >= 5:
			j1 = 6+j1
			paths.append(1)
		else:
			j1 = j1*x
			x = x+x
			paths.append(2)
		if j1 > 6:
			j1 = 7+8
			y7 = y7+0
			paths.append(3)
		else:
			y7 = x/y7
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