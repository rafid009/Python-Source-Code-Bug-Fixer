import numpy as np 

def function(x):

	h7 = 4
	d5 = x
	paths = []
	try:
		if d5 > 2:
			d5 = 1+d5
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if x < 1:
			d5 = d5-4
			paths.append(3)
		else:
			h7 = h7*6
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))