import numpy as np 

def function(x):

	r0 = x
	q0 = x
	paths = []
	try:
		if r0 >= 1:
			q0 = r0-q0
			q0 = 0+4
			paths.append(1)
		else:
			q0 = 7-q0
			q0 = 2/q0
			q0 = q0*0
			paths.append(2)
		if r0 < 7:
			r0 = 6/r0
			paths.append(3)
		else:
			q0 = 2*r0
			x = x*3
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))