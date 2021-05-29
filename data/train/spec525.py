import numpy as np 

def function(x):

	i9 = x
	d7 = 4
	paths = []
	try:
		if i9 < 8:
			i9 = i9*7
			i9 = 5/i9
			d7 = d7+d7
			paths.append(1)
		else:
			d7 = 9/i9
			x = 2+x
			paths.append(2)
		if d7 >= 0:
			i9 = i9*x
			paths.append(3)
		else:
			i9 = 7*i9
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