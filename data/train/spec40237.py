import numpy as np 

def function(x):

	t2 = 8
	d5 = 4
	paths = []
	try:
		if x >= 9:
			x = x+8
			d5 = d5-2
			paths.append(1)
		else:
			x = 7-x
			t2 = 8*6
			x = x*d5
			paths.append(2)
		if x > 2:
			x = t2*x
			d5 = x/8
			paths.append(3)
		else:
			d5 = d5-d5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))