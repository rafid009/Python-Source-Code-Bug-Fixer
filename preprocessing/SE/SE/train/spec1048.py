import numpy as np 

def function(x):

	e1 = 2
	r4 = 3
	paths = []
	try:
		if r4 > 0:
			r4 = 7/r4
			paths.append(1)
		else:
			x = 5*x
			e1 = e1+5
			paths.append(2)
		if r4 >= 8:
			r4 = r4+8
			e1 = 5*4
			r4 = r4/5
			paths.append(3)
		else:
			r4 = r4-0
			r4 = 7+6
			e1 = 1-5
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		r4 = e1**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))