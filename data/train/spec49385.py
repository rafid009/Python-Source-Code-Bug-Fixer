import numpy as np 

def function(x):

	d2 = x
	t8 = x
	paths = []
	try:
		if d2 <= 1:
			t8 = t8+6
			paths.append(1)
		else:
			d2 = d2/6
			d2 = x/d2
			t8 = 0/x
			paths.append(2)
		if x > 7:
			d2 = 9-t8
			t8 = t8*3
			paths.append(3)
		else:
			t8 = x*t8
			t8 = t8/7
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))