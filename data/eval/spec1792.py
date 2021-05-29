import numpy as np 

def function(x):

	t0 = 8
	b0 = 6
	paths = []
	try:
		if t0 >= 3:
			t0 = t0+9
			t0 = b0/t0
			paths.append(1)
		else:
			t0 = t0*4
			paths.append(2)
		if x > 7:
			b0 = b0/4
			b0 = b0-6
			b0 = b0-8
			paths.append(3)
		else:
			b0 = b0/t0
			b0 = 2-b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))