import numpy as np 

def function(x):

	q5 = 6
	r0 = x
	x = x
	paths = []
	try:
		if q5 < 7:
			x = r0/8
			r0 = 8/8
			q5 = q5-6
			paths.append(1)
		else:
			q5 = 2+2
			r0 = r0*r0
			paths.append(2)
		if q5 <= 5:
			q5 = q5*4
			q5 = 9*q5
			r0 = 0*r0
			paths.append(3)
		else:
			q5 = x-2
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