import numpy as np 

def function(x):

	t6 = 7
	e0 = 1
	paths = []
	try:
		if x < 9:
			x = x/7
			e0 = e0/x
			x = x*5
			paths.append(1)
		else:
			x = x+e0
			x = x/x
			paths.append(2)
		if t6 <= 1:
			x = e0*x
			t6 = x-e0
			t6 = 7*t6
			paths.append(3)
		else:
			x = x*t6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))