import numpy as np 

def function(x):

	y3 = 4
	j3 = x
	paths = []
	try:
		if x <= 0:
			x = j3*j3
			j3 = j3+j3
			paths.append(1)
		else:
			j3 = y3/j3
			paths.append(2)
		if x >= 2:
			j3 = j3/3
			paths.append(3)
		else:
			x = 6/j3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))