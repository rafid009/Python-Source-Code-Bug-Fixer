import numpy as np 

def function(x):

	u6 = 6
	w3 = 3
	paths = []
	try:
		if u6 < 0:
			x = x-8
			u6 = 2+u6
			w3 = 0/u6
			paths.append(1)
		else:
			w3 = w3/2
			paths.append(2)
		if u6 >= 7:
			w3 = w3-8
			u6 = 0+w3
			paths.append(3)
		else:
			w3 = 6+w3
			w3 = u6+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))