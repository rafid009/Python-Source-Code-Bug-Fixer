import numpy as np 

def function(x):

	x6 = 5
	j6 = x
	paths = []
	try:
		if j6 <= 0:
			j6 = 5/j6
			x6 = x6*4
			x6 = 3/x6
			paths.append(1)
		else:
			x = x-7
			j6 = j6-8
			x6 = 7/x6
			paths.append(2)
		if j6 >= 5:
			j6 = 0-8
			paths.append(3)
		else:
			x6 = x*x6
			j6 = 8+5
			j6 = 7-x6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x6 = j6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))