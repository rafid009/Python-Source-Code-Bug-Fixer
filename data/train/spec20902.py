import numpy as np 

def function(x):

	j4 = 3
	c2 = x
	paths = []
	try:
		if j4 > 4:
			c2 = c2/j4
			paths.append(1)
		else:
			j4 = 6-c2
			paths.append(2)
		if c2 <= 7:
			x = j4*x
			j4 = 3-j4
			x = 4-3
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))