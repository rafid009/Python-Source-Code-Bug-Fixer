import numpy as np 

def function(x):

	t0 = x
	h1 = 6
	paths = []
	try:
		if t0 >= 1:
			x = 2+x
			t0 = 2-1
			paths.append(1)
		else:
			x = t0-9
			paths.append(2)
		if t0 > 5:
			t0 = t0/7
			paths.append(3)
		else:
			x = 3+x
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