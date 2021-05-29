import numpy as np 

def function(x):

	c2 = x
	j4 = x
	x = x
	paths = []
	try:
		if c2 > 2:
			c2 = j4-c2
			paths.append(1)
		else:
			c2 = c2/4
			j4 = j4-x
			paths.append(2)
		if c2 < 9:
			j4 = 8+1
			j4 = 8*j4
			j4 = 7/j4
			paths.append(3)
		else:
			j4 = 5-j4
			c2 = x*c2
			j4 = 5*5
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))