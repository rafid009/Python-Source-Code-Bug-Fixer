import numpy as np 

def function(x):

	e0 = x
	t0 = x
	paths = []
	try:
		if x <= 9:
			e0 = e0+5
			paths.append(1)
		else:
			t0 = 6+t0
			e0 = x-9
			t0 = e0-t0
			paths.append(2)
		if x >= 4:
			x = 2+1
			x = t0+x
			t0 = t0*x
			paths.append(3)
		else:
			x = x-x
			x = 6+9
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))