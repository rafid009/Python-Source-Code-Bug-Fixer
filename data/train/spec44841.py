import numpy as np 

def function(x):

	c5 = x
	f5 = 7
	paths = []
	try:
		if x <= 2:
			f5 = f5+2
			paths.append(1)
		else:
			f5 = 0-1
			f5 = x/f5
			paths.append(2)
		if f5 <= 6:
			c5 = c5*f5
			paths.append(3)
		else:
			f5 = 3+x
			c5 = c5/c5
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))