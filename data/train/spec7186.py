import numpy as np 

def function(x):

	d7 = 2
	i7 = x
	paths = []
	try:
		if i7 >= 9:
			i7 = i7*d7
			paths.append(1)
		else:
			x = 1/x
			x = 4-6
			i7 = i7*3
			paths.append(2)
		if x <= 5:
			i7 = 8+3
			paths.append(3)
		else:
			d7 = 9+x
			i7 = i7+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))