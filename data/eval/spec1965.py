import numpy as np 

def function(x):

	c9 = x
	h7 = x
	x = x
	paths = []
	try:
		if c9 > 4:
			x = x/4
			paths.append(1)
		else:
			x = c9/3
			paths.append(2)
		if c9 >= 7:
			h7 = 8/h7
			x = x-8
			paths.append(3)
		else:
			x = x+2
			h7 = x*h7
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		h7 = c9**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))