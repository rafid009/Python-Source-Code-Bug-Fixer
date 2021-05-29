import numpy as np 

def function(x):

	r4 = 4
	t8 = 0
	paths = []
	try:
		if x >= 6:
			x = x*6
			r4 = r4*r4
			t8 = t8-t8
			paths.append(1)
		else:
			r4 = r4+r4
			paths.append(2)
		if r4 > 3:
			x = 3/x
			paths.append(3)
		else:
			t8 = 3+7
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))