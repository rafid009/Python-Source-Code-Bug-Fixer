import numpy as np 

def function(x):

	f9 = x
	c7 = 3
	paths = []
	try:
		if c7 < 9:
			c7 = x/7
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if x < 6:
			f9 = 4-f9
			x = f9-x
			paths.append(3)
		else:
			x = 3+x
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