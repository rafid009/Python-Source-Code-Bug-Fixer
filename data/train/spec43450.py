import numpy as np 

def function(x):

	t2 = 1
	d3 = x
	paths = []
	try:
		if d3 >= 3:
			x = x+8
			x = t2*d3
			t2 = t2*x
			paths.append(1)
		else:
			x = 8/t2
			paths.append(2)
		if x >= 8:
			t2 = t2*d3
			t2 = t2/1
			paths.append(3)
		else:
			x = x*5
			x = 1-9
			t2 = t2*6
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))