import numpy as np 

def function(x):

	c8 = x
	f1 = x
	paths = []
	try:
		if c8 > 0:
			c8 = c8+c8
			paths.append(1)
		else:
			c8 = c8-3
			f1 = f1*7
			paths.append(2)
		if x < 4:
			x = f1/8
			paths.append(3)
		else:
			f1 = 0*5
			x = x-c8
			f1 = x-5
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		f1 = c8**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))