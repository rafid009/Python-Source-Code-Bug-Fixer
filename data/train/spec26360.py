import numpy as np 

def function(x):

	d3 = 2
	f8 = 1
	paths = []
	try:
		if d3 < 2:
			x = x+8
			x = 9-f8
			x = 4+3
			paths.append(1)
		else:
			d3 = d3+8
			paths.append(2)
		if x < 4:
			d3 = d3-x
			f8 = 1*x
			paths.append(3)
		else:
			x = x+0
			x = x/3
			f8 = f8*f8
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))