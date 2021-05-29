import numpy as np 

def function(x):

	e2 = 3
	t8 = 7
	paths = []
	try:
		if x < 4:
			e2 = e2*e2
			e2 = e2/e2
			e2 = 1/e2
			paths.append(1)
		else:
			x = x/9
			e2 = 7+e2
			x = x*7
			paths.append(2)
		if x >= 5:
			x = x*x
			t8 = 0*t8
			x = x*e2
			paths.append(3)
		else:
			t8 = t8/x
			t8 = 9+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))