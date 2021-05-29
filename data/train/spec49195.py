import numpy as np 

def function(x):

	j6 = 6
	x5 = 1
	paths = []
	try:
		if x > 2:
			x = x*5
			j6 = j6/j6
			paths.append(1)
		else:
			j6 = x5*8
			j6 = 6-j6
			paths.append(2)
		if j6 > 8:
			j6 = x5-8
			paths.append(3)
		else:
			x5 = x-x5
			j6 = 4-x5
			j6 = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))