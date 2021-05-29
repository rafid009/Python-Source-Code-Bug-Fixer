import numpy as np 

def function(x):

	o2 = 8
	q0 = 9
	paths = []
	try:
		if o2 <= 7:
			o2 = o2*x
			q0 = o2-q0
			paths.append(1)
		else:
			o2 = o2/x
			q0 = q0/7
			paths.append(2)
		if x > 5:
			q0 = 0*q0
			x = 7-x
			paths.append(3)
		else:
			q0 = q0-o2
			q0 = q0+o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		q0 = o2**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))