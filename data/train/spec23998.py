import numpy as np 

def function(x):

	h5 = x
	q2 = x
	paths = []
	try:
		if q2 <= 4:
			x = x+x
			paths.append(1)
		else:
			q2 = q2-8
			paths.append(2)
		if x > 3:
			x = x*2
			h5 = h5/7
			paths.append(3)
		else:
			q2 = 6*4
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