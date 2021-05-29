import numpy as np 

def function(x):

	f7 = 0
	c3 = 4
	paths = []
	try:
		if c3 <= 0:
			f7 = f7/5
			f7 = f7+f7
			paths.append(1)
		else:
			x = 5*c3
			c3 = 3-c3
			f7 = c3-8
			paths.append(2)
		if c3 >= 0:
			c3 = c3/8
			x = 8-x
			paths.append(3)
		else:
			f7 = 1+7
			x = 3*c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		f7 = c3**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))