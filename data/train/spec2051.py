import numpy as np 

def function(x):

	p4 = 9
	q0 = x
	paths = []
	try:
		if x < 1:
			x = 5*x
			paths.append(1)
		else:
			p4 = 7*p4
			p4 = p4+q0
			paths.append(2)
		if q0 >= 0:
			x = x+x
			p4 = 3-x
			x = 9*q0
			paths.append(3)
		else:
			q0 = q0/8
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