import numpy as np 

def function(x):

	c2 = x
	j9 = 6
	paths = []
	try:
		if c2 <= 0:
			j9 = 2+j9
			j9 = c2*9
			paths.append(1)
		else:
			j9 = 3/1
			j9 = j9+5
			c2 = c2*c2
			paths.append(2)
		if x < 8:
			c2 = c2+2
			paths.append(3)
		else:
			x = j9-x
			j9 = 1+j9
			x = 4-j9
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))