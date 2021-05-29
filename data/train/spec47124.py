import numpy as np 

def function(x):

	t8 = x
	d3 = 1
	paths = []
	try:
		if x < 3:
			d3 = 8+x
			paths.append(1)
		else:
			t8 = 1-t8
			t8 = 3+t8
			d3 = x/8
			paths.append(2)
		if d3 >= 1:
			d3 = d3-t8
			x = x-6
			x = 2-x
			paths.append(3)
		else:
			x = t8+9
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