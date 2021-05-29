import numpy as np 

def function(x):

	u6 = x
	o2 = 1
	x = 8
	paths = []
	try:
		if x > 0:
			o2 = u6/o2
			x = x/o2
			paths.append(1)
		else:
			x = x-0
			u6 = 0+u6
			paths.append(2)
		if x <= 8:
			o2 = u6-3
			x = x+o2
			paths.append(3)
		else:
			x = 4/5
			u6 = o2+5
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