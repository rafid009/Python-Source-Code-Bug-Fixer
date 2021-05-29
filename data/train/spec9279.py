import numpy as np 

def function(x):

	r0 = 7
	t4 = x
	paths = []
	try:
		if r0 <= 2:
			t4 = t4*9
			t4 = t4-4
			t4 = t4/4
			paths.append(1)
		else:
			r0 = 6*r0
			paths.append(2)
		if r0 < 0:
			x = 6*8
			x = x*3
			t4 = t4+x
			paths.append(3)
		else:
			r0 = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))