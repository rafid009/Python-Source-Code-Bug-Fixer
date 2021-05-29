import numpy as np 

def function(x):

	d7 = 0
	i9 = 4
	paths = []
	try:
		if i9 >= 1:
			i9 = i9+d7
			d7 = d7*7
			paths.append(1)
		else:
			d7 = d7-d7
			d7 = x*6
			paths.append(2)
		if x <= 7:
			d7 = x*d7
			i9 = i9+3
			d7 = x/3
			paths.append(3)
		else:
			x = 9-6
			i9 = d7/i9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))