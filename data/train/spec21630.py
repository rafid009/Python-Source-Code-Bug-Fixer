import numpy as np 

def function(x):

	j8 = 6
	j4 = x
	paths = []
	try:
		if j4 <= 0:
			x = 7*5
			x = 6/x
			paths.append(1)
		else:
			j8 = j4-9
			paths.append(2)
		if j8 <= 7:
			x = 7*x
			j4 = 9*j4
			j4 = j8-x
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))