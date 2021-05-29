import numpy as np 

def function(x):

	x5 = 4
	v8 = 7
	paths = []
	try:
		if x >= 6:
			x = x+6
			v8 = 4-v8
			x5 = 0+x5
			paths.append(1)
		else:
			x5 = 4/v8
			v8 = 8-v8
			paths.append(2)
		if x5 >= 2:
			x5 = 5-x5
			x = 0*x
			paths.append(3)
		else:
			x = x-v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x5 = v8**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))