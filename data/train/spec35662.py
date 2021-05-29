import numpy as np 

def function(x):

	h4 = 0
	d1 = 2
	paths = []
	try:
		if d1 > 1:
			h4 = h4+x
			d1 = d1+x
			d1 = d1/3
			paths.append(1)
		else:
			x = x*7
			h4 = h4-x
			paths.append(2)
		if x > 5:
			h4 = h4*8
			x = x+d1
			paths.append(3)
		else:
			h4 = h4/d1
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))