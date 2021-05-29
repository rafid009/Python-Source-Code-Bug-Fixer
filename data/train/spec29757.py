import numpy as np 

def function(x):

	d8 = x
	t9 = 1
	paths = []
	try:
		if x >= 6:
			d8 = d8*x
			x = x+t9
			x = d8*x
			paths.append(1)
		else:
			t9 = 6-t9
			paths.append(2)
		if t9 > 1:
			t9 = 5*t9
			paths.append(3)
		else:
			d8 = 1-d8
			x = 7*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))