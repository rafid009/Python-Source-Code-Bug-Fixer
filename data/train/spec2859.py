import numpy as np 

def function(x):

	x5 = 1
	v9 = 5
	x = 5
	paths = []
	try:
		if x5 >= 9:
			x = 4*x
			x5 = v9/x5
			paths.append(1)
		else:
			v9 = v9-9
			x5 = 1+x5
			v9 = v9/x5
			paths.append(2)
		if v9 < 2:
			x5 = x5-x
			paths.append(3)
		else:
			v9 = v9/8
			v9 = v9+x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))