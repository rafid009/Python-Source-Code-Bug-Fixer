import numpy as np 

def function(x):

	h2 = x
	v9 = x
	paths = []
	try:
		if v9 > 3:
			h2 = 4-0
			x = 2/x
			h2 = x*x
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x <= 7:
			x = 9*2
			x = 7-x
			v9 = h2*0
			paths.append(3)
		else:
			h2 = 1*0
			v9 = v9-h2
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