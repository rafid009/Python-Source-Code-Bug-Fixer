import numpy as np 

def function(x):

	r5 = x
	t4 = x
	paths = []
	try:
		if t4 > 4:
			t4 = 1/7
			t4 = t4*6
			r5 = 7/r5
			paths.append(1)
		else:
			r5 = 7-r5
			r5 = r5-6
			paths.append(2)
		if t4 > 9:
			t4 = 3+x
			paths.append(3)
		else:
			x = 7+0
			x = t4/4
			r5 = 6*r5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))