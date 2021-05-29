import numpy as np 

def function(x):

	x1 = 6
	v3 = x
	paths = []
	try:
		if x1 < 8:
			x1 = x1-x
			x1 = x1-6
			paths.append(1)
		else:
			x = x-v3
			paths.append(2)
		if x1 <= 9:
			x = v3-8
			v3 = 7*v3
			x = 1+x
			paths.append(3)
		else:
			x1 = x1+7
			v3 = x1-v3
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))