import numpy as np 

def function(x):

	u6 = 2
	w9 = 6
	paths = []
	try:
		if x > 6:
			x = 1-0
			x = x+2
			paths.append(1)
		else:
			x = u6+x
			w9 = 5+w9
			paths.append(2)
		if u6 >= 6:
			u6 = 5*6
			u6 = 5-w9
			w9 = x+4
			paths.append(3)
		else:
			u6 = 8-u6
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