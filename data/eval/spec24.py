import numpy as np 

def function(x):

	d3 = x
	i9 = x
	paths = []
	try:
		if x < 8:
			i9 = i9*i9
			paths.append(1)
		else:
			i9 = 4+i9
			d3 = 5*7
			paths.append(2)
		if i9 >= 8:
			d3 = d3+8
			i9 = d3+i9
			x = 9+x
			paths.append(3)
		else:
			i9 = i9+d3
			x = x+x
			i9 = 3*x
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