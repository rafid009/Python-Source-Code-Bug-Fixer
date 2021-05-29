import numpy as np 

def function(x):

	v3 = x
	x9 = 6
	x = 6
	paths = []
	try:
		if x < 4:
			x9 = x9+5
			x9 = x9-1
			v3 = v3-4
			paths.append(1)
		else:
			x = 2+7
			x9 = x9-v3
			paths.append(2)
		if x9 > 8:
			x9 = 7*x9
			paths.append(3)
		else:
			x9 = x9+6
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		v3 = x9**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))