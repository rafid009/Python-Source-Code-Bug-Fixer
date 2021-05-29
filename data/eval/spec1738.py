import numpy as np 

def function(x):

	c9 = 5
	f4 = 3
	paths = []
	try:
		if x >= 6:
			c9 = 8+2
			c9 = 8/c9
			paths.append(1)
		else:
			c9 = 9+8
			c9 = f4/c9
			f4 = f4/9
			paths.append(2)
		if f4 >= 6:
			x = x*4
			paths.append(3)
		else:
			f4 = 6+5
			c9 = c9/x
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		f4 = c9**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))