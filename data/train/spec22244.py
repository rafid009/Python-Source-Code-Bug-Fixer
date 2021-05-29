import numpy as np 

def function(x):

	e5 = 7
	t0 = 4
	paths = []
	try:
		if x <= 4:
			x = x+e5
			t0 = t0*x
			t0 = 9*2
			paths.append(1)
		else:
			t0 = 8+x
			e5 = x+x
			paths.append(2)
		if e5 <= 1:
			e5 = e5-3
			t0 = 5/e5
			paths.append(3)
		else:
			t0 = 1-6
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