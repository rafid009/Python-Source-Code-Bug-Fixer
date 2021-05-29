import numpy as np 

def function(x):

	e3 = x
	u7 = x
	paths = []
	try:
		if u7 <= 0:
			e3 = e3+3
			paths.append(1)
		else:
			x = e3-7
			u7 = 3*x
			x = e3-7
			paths.append(2)
		if x <= 0:
			x = 1/x
			e3 = e3*1
			paths.append(3)
		else:
			e3 = 6+e3
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))