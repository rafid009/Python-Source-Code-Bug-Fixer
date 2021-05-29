import numpy as np 

def function(x):

	n7 = x
	c2 = 5
	paths = []
	try:
		if n7 >= 8:
			n7 = n7*7
			n7 = n7-5
			paths.append(1)
		else:
			n7 = 0/n7
			n7 = n7+x
			c2 = c2+n7
			paths.append(2)
		if c2 >= 4:
			n7 = 3-x
			c2 = c2+x
			x = x*8
			paths.append(3)
		else:
			c2 = 9+x
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		n7 = c2**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))