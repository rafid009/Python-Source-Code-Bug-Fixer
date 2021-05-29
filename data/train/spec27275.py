import numpy as np 

def function(x):

	r0 = x
	q9 = x
	paths = []
	try:
		if x > 2:
			r0 = q9-8
			x = 1+r0
			q9 = q9+3
			paths.append(1)
		else:
			q9 = x+0
			q9 = 0-4
			x = 4/x
			paths.append(2)
		if q9 < 1:
			r0 = 4/r0
			paths.append(3)
		else:
			x = x+2
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