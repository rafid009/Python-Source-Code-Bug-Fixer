import numpy as np 

def function(x):

	i2 = 9
	j4 = 8
	paths = []
	try:
		if x <= 0:
			j4 = 8+4
			j4 = j4+6
			paths.append(1)
		else:
			x = 0-x
			x = 3/x
			paths.append(2)
		if i2 >= 2:
			j4 = 3-j4
			paths.append(3)
		else:
			x = 7+1
			i2 = i2*9
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))