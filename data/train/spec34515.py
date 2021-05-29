import numpy as np 

def function(x):

	h2 = x
	c3 = x
	paths = []
	try:
		if c3 <= 5:
			c3 = 3+c3
			x = 4-1
			paths.append(1)
		else:
			h2 = h2+8
			paths.append(2)
		if x < 6:
			h2 = 7+c3
			paths.append(3)
		else:
			h2 = h2/c3
			x = x*2
			x = 1*c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))