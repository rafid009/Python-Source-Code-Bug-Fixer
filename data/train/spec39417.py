import numpy as np 

def function(x):

	h8 = 5
	d2 = x
	paths = []
	try:
		if x <= 6:
			h8 = 7/x
			d2 = d2+d2
			paths.append(1)
		else:
			h8 = 7-h8
			paths.append(2)
		if h8 >= 1:
			h8 = 6*6
			d2 = 1*7
			x = 2*x
			paths.append(3)
		else:
			x = 2+x
			d2 = 8*8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		d2 = h8**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))