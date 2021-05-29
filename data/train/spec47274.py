import numpy as np 

def function(x):

	c1 = 7
	f6 = 3
	paths = []
	try:
		if f6 >= 9:
			f6 = f6/c1
			c1 = x+3
			f6 = f6-3
			paths.append(1)
		else:
			c1 = 7+f6
			c1 = x-c1
			f6 = 0-5
			paths.append(2)
		if c1 <= 2:
			x = x/f6
			paths.append(3)
		else:
			f6 = f6-x
			c1 = x+4
			c1 = c1*9
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))