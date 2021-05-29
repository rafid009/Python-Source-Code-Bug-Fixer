import numpy as np 

def function(x):

	e6 = x
	h7 = 5
	paths = []
	try:
		if e6 < 7:
			h7 = x/e6
			paths.append(1)
		else:
			x = 0+x
			e6 = e6/x
			h7 = 5/5
			paths.append(2)
		if h7 <= 2:
			h7 = h7-8
			e6 = 9/e6
			paths.append(3)
		else:
			x = h7-x
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))