import numpy as np 

def function(x):

	e4 = x
	u6 = 8
	paths = []
	try:
		if x <= 9:
			u6 = u6*u6
			x = 2/x
			paths.append(1)
		else:
			u6 = u6*9
			u6 = e4/1
			e4 = 6+e4
			paths.append(2)
		if u6 <= 3:
			e4 = e4-2
			u6 = u6-2
			paths.append(3)
		else:
			e4 = e4/2
			e4 = e4+4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))