import numpy as np 

def function(x):

	t0 = x
	r5 = 8
	paths = []
	try:
		if t0 > 3:
			x = 5/5
			t0 = t0+8
			t0 = 8+9
			paths.append(1)
		else:
			t0 = 2+t0
			t0 = 0+t0
			paths.append(2)
		if x > 2:
			x = x+5
			paths.append(3)
		else:
			r5 = r5*2
			t0 = t0/2
			t0 = r5*x
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