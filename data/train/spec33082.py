import numpy as np 

def function(x):

	y4 = 1
	j5 = 3
	paths = []
	try:
		if x < 3:
			y4 = 4/j5
			j5 = j5*5
			y4 = y4+4
			paths.append(1)
		else:
			y4 = j5/y4
			j5 = j5+9
			paths.append(2)
		if x >= 2:
			j5 = 1+2
			paths.append(3)
		else:
			j5 = 7*j5
			y4 = 1/y4
			j5 = x*4
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))