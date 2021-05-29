import numpy as np 

def function(x):

	o9 = 3
	h2 = 9
	x = x
	paths = []
	try:
		if x < 9:
			h2 = 9/h2
			h2 = h2/1
			paths.append(1)
		else:
			h2 = h2+o9
			x = h2/h2
			h2 = 0-4
			paths.append(2)
		if h2 < 4:
			o9 = 9*2
			o9 = x*7
			o9 = o9/1
			paths.append(3)
		else:
			o9 = 1/o9
			h2 = h2*7
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))