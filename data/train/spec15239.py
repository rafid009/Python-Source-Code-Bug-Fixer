import numpy as np 

def function(x):

	c9 = x
	f9 = x
	paths = []
	try:
		if c9 > 9:
			f9 = x*f9
			paths.append(1)
		else:
			f9 = c9*f9
			paths.append(2)
		if c9 <= 9:
			f9 = x*f9
			f9 = f9*4
			paths.append(3)
		else:
			c9 = f9/7
			f9 = 9+f9
			c9 = c9-7
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		f9 = c9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))