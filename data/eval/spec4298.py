import numpy as np 

def function(x):

	t9 = x
	d2 = x
	x = 1
	paths = []
	try:
		if t9 >= 3:
			x = 2/x
			paths.append(1)
		else:
			x = x*t9
			paths.append(2)
		if d2 > 7:
			t9 = t9+8
			t9 = x*5
			paths.append(3)
		else:
			d2 = 5-d2
			x = x+7
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))