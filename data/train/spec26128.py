import numpy as np 

def function(x):

	a4 = x
	u6 = 3
	paths = []
	try:
		if x >= 3:
			u6 = u6+u6
			paths.append(1)
		else:
			u6 = 0+u6
			paths.append(2)
		if u6 > 5:
			a4 = 3/9
			u6 = 6+u6
			u6 = u6+4
			paths.append(3)
		else:
			a4 = 9/a4
			x = x*7
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		u6 = a4**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))