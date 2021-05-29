import numpy as np 

def function(x):

	r7 = 8
	c7 = x
	paths = []
	try:
		if x < 9:
			r7 = x/c7
			r7 = 0*r7
			c7 = c7+8
			paths.append(1)
		else:
			r7 = r7/6
			paths.append(2)
		if c7 >= 2:
			c7 = c7*8
			r7 = 2+r7
			paths.append(3)
		else:
			r7 = r7*3
			c7 = 1/c7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))