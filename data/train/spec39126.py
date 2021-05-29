import numpy as np 

def function(x):

	t0 = 0
	r7 = 8
	paths = []
	try:
		if t0 > 8:
			r7 = 3+r7
			r7 = r7/x
			r7 = t0+7
			paths.append(1)
		else:
			t0 = t0+t0
			paths.append(2)
		if t0 <= 2:
			t0 = t0/5
			r7 = r7*7
			paths.append(3)
		else:
			r7 = r7-r7
			t0 = 3*t0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))