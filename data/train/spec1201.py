import numpy as np 

def function(x):

	h2 = 8
	f4 = x
	paths = []
	try:
		if x < 9:
			x = f4*4
			h2 = 3*x
			paths.append(1)
		else:
			f4 = f4+6
			f4 = h2+f4
			f4 = x/f4
			paths.append(2)
		if h2 > 0:
			f4 = 8*f4
			f4 = f4/h2
			paths.append(3)
		else:
			f4 = f4*6
			f4 = f4+3
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		h2 = f4**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))