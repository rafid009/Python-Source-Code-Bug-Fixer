import numpy as np 

def function(x):

	t0 = x
	o1 = x
	paths = []
	try:
		if x > 3:
			t0 = t0+0
			o1 = 7-6
			paths.append(1)
		else:
			o1 = 8+o1
			t0 = 2/3
			paths.append(2)
		if x < 6:
			o1 = o1*o1
			paths.append(3)
		else:
			o1 = o1-7
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