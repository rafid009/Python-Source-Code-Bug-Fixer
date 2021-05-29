import numpy as np 

def function(x):

	c3 = x
	n5 = x
	paths = []
	try:
		if x > 5:
			n5 = 4*1
			paths.append(1)
		else:
			x = 9+1
			x = x/x
			paths.append(2)
		if n5 < 7:
			c3 = c3+4
			c3 = c3*8
			paths.append(3)
		else:
			n5 = 0+n5
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		n5 = c3**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))