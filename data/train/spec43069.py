import numpy as np 

def function(x):

	q1 = 5
	r7 = x
	paths = []
	try:
		if r7 > 1:
			x = x/r7
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x >= 7:
			r7 = r7/1
			r7 = 9*r7
			q1 = q1*3
			paths.append(3)
		else:
			r7 = r7+r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))