import numpy as np 

def function(x):

	t8 = 7
	r4 = x
	paths = []
	try:
		if x >= 2:
			t8 = 6*x
			paths.append(1)
		else:
			t8 = 6/t8
			t8 = 3-7
			r4 = r4+9
			paths.append(2)
		if r4 > 5:
			x = x*r4
			paths.append(3)
		else:
			x = x*x
			r4 = t8-r4
			r4 = t8+1
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