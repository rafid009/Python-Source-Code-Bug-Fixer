import numpy as np 

def function(x):

	r1 = 5
	q0 = x
	paths = []
	try:
		if r1 > 5:
			q0 = q0/6
			x = x+r1
			x = q0*x
			paths.append(1)
		else:
			r1 = r1*x
			q0 = q0*r1
			r1 = r1*r1
			paths.append(2)
		if q0 <= 4:
			q0 = 7/q0
			paths.append(3)
		else:
			q0 = q0/6
			r1 = r1+1
			r1 = q0-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))