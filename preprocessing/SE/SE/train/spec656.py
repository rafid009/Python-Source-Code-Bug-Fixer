import numpy as np 

def function(x):

	d5 = x
	h8 = 5
	paths = []
	try:
		if d5 <= 3:
			x = 7/x
			paths.append(1)
		else:
			x = 3*x
			d5 = d5/1
			x = x*5
			paths.append(2)
		if x <= 8:
			x = x-4
			h8 = 0-h8
			paths.append(3)
		else:
			h8 = 2/3
			d5 = 4+h8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))