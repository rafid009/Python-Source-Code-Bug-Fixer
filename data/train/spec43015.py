import numpy as np 

def function(x):

	c9 = x
	f8 = 8
	paths = []
	try:
		if f8 > 7:
			c9 = c9/5
			x = 4-3
			paths.append(1)
		else:
			x = x/x
			f8 = 3-6
			c9 = c9+8
			paths.append(2)
		if f8 <= 9:
			f8 = 5/f8
			c9 = c9+5
			c9 = 4+c9
			paths.append(3)
		else:
			f8 = 5-f8
			c9 = 5*7
			c9 = 3-6
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))