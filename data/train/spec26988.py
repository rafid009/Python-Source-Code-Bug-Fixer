import numpy as np 

def function(x):

	j6 = 6
	x4 = x
	paths = []
	try:
		if x <= 2:
			j6 = 1+x4
			j6 = 8*j6
			paths.append(1)
		else:
			j6 = 8*j6
			x4 = x4/8
			paths.append(2)
		if x4 >= 7:
			x = x-4
			x = 2/4
			paths.append(3)
		else:
			x4 = 8/j6
			j6 = 4*j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))