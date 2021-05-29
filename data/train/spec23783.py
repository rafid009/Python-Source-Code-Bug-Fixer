import numpy as np 

def function(x):

	h3 = 6
	r3 = 9
	x = x
	paths = []
	try:
		if h3 < 3:
			r3 = r3*h3
			paths.append(1)
		else:
			r3 = r3*4
			h3 = 2-6
			paths.append(2)
		if x > 5:
			h3 = 9*r3
			h3 = h3-6
			paths.append(3)
		else:
			r3 = 3-r3
			x = x+x
			h3 = h3/x
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		h3 = r3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))