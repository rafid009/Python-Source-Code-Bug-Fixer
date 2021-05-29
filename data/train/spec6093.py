import numpy as np 

def function(x):

	t0 = x
	d6 = 2
	paths = []
	try:
		if d6 < 7:
			d6 = d6+5
			paths.append(1)
		else:
			d6 = 0*9
			d6 = d6/t0
			d6 = 1*t0
			paths.append(2)
		if x >= 2:
			x = d6-9
			d6 = d6*9
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))