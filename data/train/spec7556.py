import numpy as np 

def function(x):

	n3 = x
	c9 = x
	paths = []
	try:
		if n3 >= 9:
			x = 2+2
			paths.append(1)
		else:
			c9 = 8*c9
			paths.append(2)
		if x >= 7:
			n3 = n3/x
			paths.append(3)
		else:
			c9 = 2/c9
			n3 = 5+9
			n3 = n3*n3
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		n3 = c9**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))