import numpy as np 

def function(x):

	c5 = x
	h2 = x
	paths = []
	try:
		if h2 <= 1:
			x = x-2
			h2 = 5-h2
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if c5 >= 4:
			h2 = 0*x
			paths.append(3)
		else:
			h2 = 7-5
			h2 = h2*0
			x = h2/6
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		h2 = c5**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))