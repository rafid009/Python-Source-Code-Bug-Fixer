import numpy as np 

def function(x):

	n2 = x
	q0 = 5
	paths = []
	try:
		if q0 < 7:
			x = 2*x
			x = 8*x
			paths.append(1)
		else:
			q0 = 0+8
			q0 = q0-8
			x = x/7
			paths.append(2)
		if x > 8:
			n2 = 1+n2
			paths.append(3)
		else:
			q0 = 1*n2
			n2 = 1-n2
			n2 = 2-n2
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))