import numpy as np 

def function(x):

	d0 = x
	u4 = x
	paths = []
	try:
		if u4 <= 8:
			u4 = u4*7
			paths.append(1)
		else:
			x = x+1
			x = 2/x
			u4 = 9/u4
			paths.append(2)
		if x > 2:
			x = 9*4
			paths.append(3)
		else:
			d0 = x+d0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))