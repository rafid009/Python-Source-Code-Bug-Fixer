import numpy as np 

def function(x):

	h8 = 5
	d8 = x
	paths = []
	try:
		if d8 < 3:
			d8 = 4+d8
			paths.append(1)
		else:
			x = x-8
			x = x+5
			paths.append(2)
		if h8 <= 4:
			x = x-2
			h8 = h8+d8
			h8 = 2-x
			paths.append(3)
		else:
			x = 5+3
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))