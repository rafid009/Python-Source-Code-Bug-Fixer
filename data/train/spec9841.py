import numpy as np 

def function(x):

	d2 = x
	u6 = 9
	x = x
	paths = []
	try:
		if u6 > 8:
			u6 = u6+3
			paths.append(1)
		else:
			u6 = d2*u6
			d2 = d2+2
			paths.append(2)
		if x < 5:
			d2 = d2+5
			paths.append(3)
		else:
			u6 = 3/u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))