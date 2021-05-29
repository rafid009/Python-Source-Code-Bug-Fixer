import numpy as np 

def function(x):

	h9 = 9
	d7 = x
	paths = []
	try:
		if d7 <= 5:
			h9 = 5*h9
			x = x+2
			d7 = 9/1
			paths.append(1)
		else:
			x = d7+x
			x = x*3
			d7 = x-d7
			paths.append(2)
		if x <= 4:
			h9 = h9+6
			d7 = d7*1
			h9 = h9/3
			paths.append(3)
		else:
			h9 = 4/h9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))