import numpy as np 

def function(x):

	c2 = 9
	i8 = x
	paths = []
	try:
		if i8 < 9:
			i8 = 0-0
			paths.append(1)
		else:
			i8 = 9*i8
			paths.append(2)
		if x <= 2:
			i8 = i8*4
			c2 = 4-c2
			paths.append(3)
		else:
			c2 = c2/3
			c2 = c2-6
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))