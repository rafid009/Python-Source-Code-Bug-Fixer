import numpy as np 

def function(x):

	f2 = x
	u6 = x
	x = x
	paths = []
	try:
		if u6 < 0:
			x = x+6
			u6 = 8*4
			u6 = u6/5
			paths.append(1)
		else:
			f2 = f2-3
			f2 = f2-4
			x = x+6
			paths.append(2)
		if u6 > 6:
			x = x*4
			paths.append(3)
		else:
			x = x*6
			u6 = 1/7
			u6 = u6+5
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