import numpy as np 

def function(x):

	a8 = 2
	r1 = x
	paths = []
	try:
		if a8 < 2:
			x = 3/x
			r1 = a8+7
			a8 = a8/6
			paths.append(1)
		else:
			a8 = r1-7
			r1 = r1/7
			paths.append(2)
		if r1 < 7:
			r1 = r1/a8
			paths.append(3)
		else:
			a8 = a8*4
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))