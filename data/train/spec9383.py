import numpy as np 

def function(x):

	i5 = x
	c6 = 5
	paths = []
	try:
		if x >= 1:
			i5 = 3-9
			c6 = 5-c6
			paths.append(1)
		else:
			x = x/3
			x = 3-2
			paths.append(2)
		if x > 2:
			x = 1-i5
			i5 = i5-5
			x = x*6
			paths.append(3)
		else:
			x = 9+x
			c6 = 6+c6
			x = x-9
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))