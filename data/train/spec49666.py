import numpy as np 

def function(x):

	q2 = x
	r5 = 0
	paths = []
	try:
		if r5 < 2:
			x = 2-4
			r5 = 4-2
			q2 = q2+2
			paths.append(1)
		else:
			x = x/5
			r5 = q2*r5
			paths.append(2)
		if x < 5:
			q2 = q2*q2
			r5 = r5+r5
			r5 = r5*9
			paths.append(3)
		else:
			q2 = 3-q2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))