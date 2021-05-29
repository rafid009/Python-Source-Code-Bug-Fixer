import numpy as np 

def function(x):

	t0 = x
	j5 = 7
	paths = []
	try:
		if x >= 4:
			t0 = 2-9
			x = 3*x
			j5 = j5*t0
			paths.append(1)
		else:
			t0 = 7/t0
			t0 = 2+t0
			t0 = t0+9
			paths.append(2)
		if j5 > 4:
			j5 = 9*t0
			paths.append(3)
		else:
			j5 = j5+2
			t0 = 9/7
			t0 = t0+t0
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