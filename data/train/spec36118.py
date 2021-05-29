import numpy as np 

def function(x):

	d8 = 2
	t7 = x
	paths = []
	try:
		if t7 > 8:
			x = x+5
			d8 = 6*4
			d8 = 8*d8
			paths.append(1)
		else:
			d8 = 3+4
			t7 = 7-8
			paths.append(2)
		if d8 > 8:
			d8 = d8*t7
			x = x*6
			paths.append(3)
		else:
			t7 = t7+8
			t7 = t7/t7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))