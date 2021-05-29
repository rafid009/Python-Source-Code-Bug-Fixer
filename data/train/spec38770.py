import numpy as np 

def function(x):

	r6 = 5
	r7 = 3
	paths = []
	try:
		if x < 3:
			x = r6*x
			r7 = r7-2
			r6 = 9*4
			paths.append(1)
		else:
			r7 = 2+r7
			r7 = 2*r7
			paths.append(2)
		if x > 3:
			r6 = r7/x
			r7 = r7/x
			paths.append(3)
		else:
			r7 = 9/r6
			r7 = r7-x
			x = 0*5
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r6 = r7**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))