import numpy as np 

def function(x):

	u9 = 3
	d2 = 9
	paths = []
	try:
		if u9 < 0:
			d2 = d2/d2
			d2 = d2/3
			paths.append(1)
		else:
			u9 = 1*u9
			x = x+x
			d2 = 0*d2
			paths.append(2)
		if d2 < 1:
			d2 = x*7
			paths.append(3)
		else:
			x = x*u9
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))