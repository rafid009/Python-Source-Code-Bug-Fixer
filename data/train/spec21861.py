import numpy as np 

def function(x):

	c9 = x
	h3 = 8
	paths = []
	try:
		if x < 7:
			x = c9-x
			paths.append(1)
		else:
			x = 0/5
			h3 = 0/h3
			paths.append(2)
		if c9 <= 5:
			h3 = c9-x
			paths.append(3)
		else:
			h3 = h3/c9
			h3 = 2*c9
			x = x+1
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		h3 = c9**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))