import numpy as np 

def function(x):

	j5 = 9
	y4 = 2
	paths = []
	try:
		if x < 3:
			y4 = 5/y4
			paths.append(1)
		else:
			j5 = 5+j5
			y4 = y4-0
			paths.append(2)
		if j5 <= 2:
			j5 = 7/x
			paths.append(3)
		else:
			j5 = 3*8
			j5 = j5+0
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