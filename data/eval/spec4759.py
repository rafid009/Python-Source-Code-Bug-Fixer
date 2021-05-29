import numpy as np 

def function(x):

	u7 = x
	v1 = 7
	paths = []
	try:
		if x <= 3:
			v1 = 2-5
			paths.append(1)
		else:
			v1 = v1-7
			paths.append(2)
		if u7 <= 8:
			x = 8+u7
			x = 2+x
			paths.append(3)
		else:
			x = x-u7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))