import numpy as np 

def function(x):

	j9 = x
	c4 = 8
	paths = []
	try:
		if x >= 4:
			x = 8*j9
			paths.append(1)
		else:
			c4 = c4*j9
			paths.append(2)
		if c4 > 8:
			j9 = j9/3
			c4 = c4/x
			paths.append(3)
		else:
			c4 = 5*c4
			x = 6+x
			c4 = 1+j9
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		j9 = c4**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))