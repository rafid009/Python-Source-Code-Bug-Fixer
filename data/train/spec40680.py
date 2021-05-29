import numpy as np 

def function(x):

	c1 = 2
	f7 = x
	paths = []
	try:
		if c1 > 7:
			f7 = f7+9
			paths.append(1)
		else:
			f7 = 8/f7
			paths.append(2)
		if c1 > 4:
			f7 = f7*0
			c1 = c1/8
			paths.append(3)
		else:
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))