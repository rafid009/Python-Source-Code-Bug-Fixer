import numpy as np 

def function(x):

	t2 = 2
	x3 = x
	paths = []
	try:
		if t2 < 7:
			x3 = x3+x
			x3 = x3+x3
			paths.append(1)
		else:
			t2 = t2*4
			paths.append(2)
		if x3 > 8:
			x3 = 3+6
			paths.append(3)
		else:
			x = 9*x
			t2 = x3*t2
			x = 9/x
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