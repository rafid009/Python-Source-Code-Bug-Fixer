import numpy as np 

def function(x):

	d9 = 5
	i3 = x
	paths = []
	try:
		if i3 <= 8:
			i3 = i3*9
			d9 = 7/x
			paths.append(1)
		else:
			x = 5-x
			d9 = 7-d9
			paths.append(2)
		if d9 > 4:
			d9 = d9*d9
			x = 6*d9
			x = x-2
			paths.append(3)
		else:
			d9 = 9+d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))