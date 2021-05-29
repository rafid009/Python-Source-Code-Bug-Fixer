import numpy as np 

def function(x):

	u6 = x
	n6 = 4
	paths = []
	try:
		if n6 <= 2:
			n6 = n6*7
			u6 = 0*5
			paths.append(1)
		else:
			n6 = 9+n6
			n6 = 0-6
			paths.append(2)
		if x > 7:
			u6 = 0-n6
			paths.append(3)
		else:
			u6 = 7/9
			u6 = n6*u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))