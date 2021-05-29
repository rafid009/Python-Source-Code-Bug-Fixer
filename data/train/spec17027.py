import numpy as np 

def function(x):

	u7 = x
	v6 = x
	paths = []
	try:
		if x < 5:
			x = v6+4
			paths.append(1)
		else:
			v6 = v6+x
			paths.append(2)
		if x < 6:
			u7 = 5-u7
			v6 = 0/9
			paths.append(3)
		else:
			v6 = v6/8
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