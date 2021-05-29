import numpy as np 

def function(x):

	t9 = 2
	d4 = x
	paths = []
	try:
		if d4 >= 3:
			d4 = d4-8
			t9 = t9/x
			paths.append(1)
		else:
			d4 = d4-t9
			x = 9*x
			paths.append(2)
		if x >= 4:
			x = 1+0
			d4 = d4*4
			x = 2*x
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))