import numpy as np 

def function(x):

	a7 = x
	j6 = 4
	paths = []
	try:
		if j6 >= 2:
			x = 0-a7
			paths.append(1)
		else:
			j6 = a7/7
			paths.append(2)
		if x > 5:
			j6 = a7*j6
			paths.append(3)
		else:
			x = 6*6
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		j6 = a7**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))