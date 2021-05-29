import numpy as np 

def function(x):

	c7 = x
	f3 = 3
	paths = []
	try:
		if f3 >= 0:
			f3 = f3-0
			f3 = f3/7
			paths.append(1)
		else:
			x = x-1
			c7 = c7-2
			paths.append(2)
		if f3 > 4:
			c7 = x/c7
			paths.append(3)
		else:
			x = 2+f3
			f3 = f3/c7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))