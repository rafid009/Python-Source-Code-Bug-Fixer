import numpy as np 

def function(x):

	f1 = x
	c8 = x
	paths = []
	try:
		if x >= 4:
			c8 = c8*7
			f1 = f1+9
			paths.append(1)
		else:
			f1 = x-f1
			paths.append(2)
		if f1 >= 5:
			x = 2-x
			x = x+4
			f1 = 9-f1
			paths.append(3)
		else:
			f1 = x+1
			c8 = c8*f1
			x = c8+2
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))