import numpy as np 

def function(x):

	t0 = x
	a9 = 7
	paths = []
	try:
		if x <= 7:
			x = x*2
			t0 = t0-a9
			paths.append(1)
		else:
			a9 = a9+2
			paths.append(2)
		if x >= 7:
			a9 = a9/t0
			x = x/a9
			t0 = 6*t0
			paths.append(3)
		else:
			t0 = t0*a9
			a9 = a9/7
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))