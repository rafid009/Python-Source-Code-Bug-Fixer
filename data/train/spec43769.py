import numpy as np 

def function(x):

	u6 = x
	e4 = 4
	paths = []
	try:
		if e4 <= 9:
			x = x*4
			e4 = e4-x
			e4 = x/1
			paths.append(1)
		else:
			e4 = e4+8
			paths.append(2)
		if e4 >= 7:
			u6 = 9-u6
			x = x*x
			paths.append(3)
		else:
			x = 3-x
			e4 = x/9
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		u6 = e4**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))