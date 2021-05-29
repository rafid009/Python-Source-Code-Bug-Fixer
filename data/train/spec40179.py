import numpy as np 

def function(x):

	i9 = x
	d0 = 4
	paths = []
	try:
		if i9 >= 8:
			d0 = 1*i9
			i9 = i9*i9
			x = x+2
			paths.append(1)
		else:
			x = 6-7
			paths.append(2)
		if d0 > 5:
			x = x-1
			paths.append(3)
		else:
			d0 = 6*3
			x = i9+x
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