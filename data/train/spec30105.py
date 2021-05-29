import numpy as np 

def function(x):

	v9 = x
	x9 = 7
	paths = []
	try:
		if x >= 4:
			x9 = 9/x9
			paths.append(1)
		else:
			x9 = 5+x9
			x9 = v9+3
			paths.append(2)
		if x9 >= 7:
			v9 = v9+9
			paths.append(3)
		else:
			x9 = 3+x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		v9 = x9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))