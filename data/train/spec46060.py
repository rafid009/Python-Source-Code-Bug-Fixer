import numpy as np 

def function(x):

	c7 = x
	n3 = x
	paths = []
	try:
		if n3 <= 7:
			n3 = n3/9
			paths.append(1)
		else:
			c7 = 1-n3
			n3 = 4/n3
			paths.append(2)
		if n3 > 3:
			n3 = n3+3
			x = 8/n3
			n3 = n3/4
			paths.append(3)
		else:
			x = x+n3
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		n3 = c7**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))