import numpy as np 

def function(x):

	d8 = 3
	i5 = x
	paths = []
	try:
		if x >= 5:
			i5 = i5+i5
			x = 7*7
			paths.append(1)
		else:
			d8 = x/x
			paths.append(2)
		if d8 >= 0:
			d8 = d8*x
			x = x/3
			paths.append(3)
		else:
			x = x/i5
			d8 = d8-9
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))