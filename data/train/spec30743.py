import numpy as np 

def function(x):

	u6 = 8
	e5 = 9
	paths = []
	try:
		if u6 <= 1:
			x = 9+e5
			x = x+0
			paths.append(1)
		else:
			x = u6*x
			e5 = 4*e5
			paths.append(2)
		if x <= 6:
			e5 = 8-1
			u6 = u6-u6
			u6 = u6+2
			paths.append(3)
		else:
			e5 = 1-x
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))