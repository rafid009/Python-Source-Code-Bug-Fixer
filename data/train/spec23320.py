import numpy as np 

def function(x):

	t2 = 5
	d3 = x
	paths = []
	try:
		if t2 > 0:
			t2 = 2*9
			paths.append(1)
		else:
			t2 = 6+1
			d3 = x-4
			t2 = 4*6
			paths.append(2)
		if x > 1:
			t2 = t2*t2
			x = 2-9
			t2 = t2+4
			paths.append(3)
		else:
			x = x/3
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