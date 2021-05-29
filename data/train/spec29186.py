import numpy as np 

def function(x):

	n7 = 4
	u0 = 4
	paths = []
	try:
		if n7 > 4:
			u0 = u0-3
			x = 7-7
			paths.append(1)
		else:
			x = x*7
			u0 = u0-7
			n7 = u0-6
			paths.append(2)
		if u0 >= 1:
			u0 = u0*2
			x = x+n7
			paths.append(3)
		else:
			u0 = u0/1
			u0 = u0*1
			u0 = u0+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))