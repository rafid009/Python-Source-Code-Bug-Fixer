import numpy as np 

def function(x):

	x2 = 1
	c1 = x
	paths = []
	try:
		if x2 > 5:
			x = x/x
			x = x+1
			paths.append(1)
		else:
			x = 9+c1
			x2 = x2/9
			paths.append(2)
		if x < 2:
			c1 = 8-9
			x = x-6
			x2 = 1-x2
			paths.append(3)
		else:
			x2 = 9+3
			x2 = 6+x2
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x2 = c1**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))