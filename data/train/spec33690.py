import numpy as np 

def function(x):

	r6 = x
	t0 = 9
	paths = []
	try:
		if t0 <= 7:
			t0 = t0*4
			x = 7-x
			paths.append(1)
		else:
			t0 = t0+8
			paths.append(2)
		if r6 > 5:
			t0 = t0-t0
			t0 = 1+t0
			paths.append(3)
		else:
			r6 = r6-t0
			t0 = 1-8
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