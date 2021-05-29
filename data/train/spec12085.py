import numpy as np 

def function(x):

	j1 = 8
	y2 = x
	paths = []
	try:
		if j1 >= 7:
			j1 = j1/6
			x = 0-x
			x = 0-x
			paths.append(1)
		else:
			y2 = 2-x
			y2 = 8/x
			paths.append(2)
		if x < 2:
			x = y2*9
			j1 = y2*1
			y2 = 7*9
			paths.append(3)
		else:
			j1 = j1+4
			x = y2/x
			j1 = 4/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))