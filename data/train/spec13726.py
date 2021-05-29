import numpy as np 

def function(x):

	n3 = x
	q0 = 3
	paths = []
	try:
		if q0 <= 2:
			q0 = 1+q0
			q0 = q0*q0
			q0 = 9*q0
			paths.append(1)
		else:
			n3 = 6/1
			n3 = n3-3
			paths.append(2)
		if n3 >= 8:
			x = x*2
			x = 2+x
			paths.append(3)
		else:
			n3 = n3*x
			n3 = 7*n3
			q0 = q0*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))