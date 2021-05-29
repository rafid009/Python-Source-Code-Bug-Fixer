import numpy as np 

def function(x):

	q2 = 0
	r1 = x
	paths = []
	try:
		if x > 5:
			r1 = 2+r1
			x = 6+r1
			paths.append(1)
		else:
			x = 2/x
			q2 = 3-q2
			paths.append(2)
		if q2 < 2:
			x = x-4
			x = 7/6
			r1 = q2-q2
			paths.append(3)
		else:
			x = x+1
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