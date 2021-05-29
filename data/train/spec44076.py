import numpy as np 

def function(x):

	c6 = x
	f5 = 6
	paths = []
	try:
		if f5 >= 2:
			f5 = f5+0
			x = x-5
			paths.append(1)
		else:
			c6 = 2-c6
			x = 8*0
			paths.append(2)
		if f5 >= 1:
			x = 1-x
			c6 = 5*0
			c6 = c6/8
			paths.append(3)
		else:
			f5 = f5+c6
			x = x/c6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))