import numpy as np 

def function(x):

	c4 = x
	f9 = x
	paths = []
	try:
		if f9 < 7:
			c4 = f9*9
			x = 7/4
			c4 = x*x
			paths.append(1)
		else:
			c4 = 0-9
			x = x*5
			f9 = 1*c4
			paths.append(2)
		if f9 <= 9:
			c4 = 1-c4
			c4 = c4/3
			paths.append(3)
		else:
			c4 = 4*7
			x = x-2
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))