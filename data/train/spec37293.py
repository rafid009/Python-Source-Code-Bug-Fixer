import numpy as np 

def function(x):

	n7 = x
	c1 = x
	paths = []
	try:
		if c1 <= 5:
			n7 = 3-n7
			c1 = c1*1
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if x >= 3:
			n7 = n7/2
			paths.append(3)
		else:
			n7 = n7*x
			x = 9+1
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))