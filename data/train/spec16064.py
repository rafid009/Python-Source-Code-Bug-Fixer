import numpy as np 

def function(x):

	t7 = 2
	d3 = x
	paths = []
	try:
		if t7 >= 2:
			t7 = d3-6
			d3 = 3/d3
			d3 = t7*d3
			paths.append(1)
		else:
			d3 = 3-4
			x = 3+4
			paths.append(2)
		if d3 > 7:
			d3 = 2/5
			paths.append(3)
		else:
			t7 = 7*t7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))