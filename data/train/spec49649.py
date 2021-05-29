import numpy as np 

def function(x):

	c7 = x
	d8 = 5
	paths = []
	try:
		if x >= 9:
			d8 = 2-c7
			x = x-6
			paths.append(1)
		else:
			c7 = c7*7
			d8 = d8*0
			d8 = 5-d8
			paths.append(2)
		if x >= 1:
			x = x/3
			d8 = d8+1
			paths.append(3)
		else:
			d8 = c7*9
			x = 0-6
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))