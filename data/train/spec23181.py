import numpy as np 

def function(x):

	a6 = 7
	r4 = 8
	paths = []
	try:
		if a6 > 4:
			r4 = x/r4
			a6 = r4-7
			paths.append(1)
		else:
			r4 = 6*r4
			a6 = a6+1
			x = a6/7
			paths.append(2)
		if r4 < 9:
			r4 = 8+r4
			a6 = a6+5
			x = x-1
			paths.append(3)
		else:
			x = r4*x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		r4 = a6**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))