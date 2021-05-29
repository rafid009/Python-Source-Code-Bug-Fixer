import numpy as np 

def function(x):

	d0 = x
	u9 = x
	paths = []
	try:
		if x < 2:
			d0 = d0-8
			u9 = 8/u9
			paths.append(1)
		else:
			u9 = x/d0
			d0 = 1+x
			x = 4+u9
			paths.append(2)
		if x < 5:
			d0 = d0*5
			x = x*8
			d0 = 7+d0
			paths.append(3)
		else:
			x = 5*x
			u9 = 9+3
			d0 = d0/6
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))