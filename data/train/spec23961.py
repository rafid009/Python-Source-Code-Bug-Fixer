import numpy as np 

def function(x):

	c3 = x
	f7 = 7
	paths = []
	try:
		if x < 0:
			x = 7/x
			x = 3/4
			paths.append(1)
		else:
			c3 = c3/c3
			paths.append(2)
		if f7 > 5:
			c3 = x+c3
			f7 = f7-x
			x = x-x
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))