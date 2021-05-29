import numpy as np 

def function(x):

	u4 = x
	d2 = 5
	paths = []
	try:
		if x > 7:
			d2 = u4/d2
			paths.append(1)
		else:
			u4 = x/7
			paths.append(2)
		if d2 > 4:
			d2 = d2/5
			d2 = 1-d2
			paths.append(3)
		else:
			u4 = u4/4
			u4 = 8-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))