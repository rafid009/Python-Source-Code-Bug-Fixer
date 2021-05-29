import numpy as np 

def function(x):

	y3 = 1
	j7 = 2
	paths = []
	try:
		if x >= 3:
			y3 = j7-2
			j7 = j7-0
			x = x+5
			paths.append(1)
		else:
			j7 = 1/j7
			paths.append(2)
		if y3 < 0:
			x = j7+x
			paths.append(3)
		else:
			j7 = j7+j7
			y3 = y3-7
			j7 = j7-7
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))