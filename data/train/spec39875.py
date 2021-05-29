import numpy as np 

def function(x):

	d3 = x
	t5 = 2
	paths = []
	try:
		if x <= 1:
			x = x-x
			d3 = d3-1
			t5 = t5/t5
			paths.append(1)
		else:
			t5 = 2*t5
			d3 = d3+x
			x = x-8
			paths.append(2)
		if x >= 7:
			x = x+2
			x = 7+x
			paths.append(3)
		else:
			d3 = x*d3
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