import numpy as np 

def function(x):

	t5 = 0
	t0 = x
	x = 3
	paths = []
	try:
		if x > 2:
			t5 = t5-4
			x = 0*x
			paths.append(1)
		else:
			t5 = t5+x
			paths.append(2)
		if t5 < 7:
			t5 = 3+t0
			paths.append(3)
		else:
			x = t5*x
			x = x-x
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