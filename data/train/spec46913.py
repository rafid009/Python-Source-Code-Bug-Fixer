import numpy as np 

def function(x):

	h2 = 0
	c3 = x
	paths = []
	try:
		if c3 >= 6:
			x = c3+x
			paths.append(1)
		else:
			c3 = 1+c3
			x = x*0
			h2 = h2+7
			paths.append(2)
		if x > 0:
			h2 = 4+h2
			c3 = 2+5
			x = 4-x
			paths.append(3)
		else:
			h2 = h2-h2
			x = 3-c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		h2 = c3**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))