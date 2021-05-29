import numpy as np 

def function(x):

	t8 = x
	d4 = x
	paths = []
	try:
		if t8 <= 4:
			t8 = 1*5
			d4 = 5/x
			t8 = 8*t8
			paths.append(1)
		else:
			d4 = 8/x
			paths.append(2)
		if x > 1:
			x = 4/x
			d4 = d4*5
			t8 = t8-t8
			paths.append(3)
		else:
			x = x+6
			x = x*3
			d4 = 4-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))