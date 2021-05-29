import numpy as np 

def function(x):

	q2 = 7
	v2 = 1
	paths = []
	try:
		if x >= 2:
			v2 = v2*q2
			q2 = q2*v2
			q2 = x+q2
			paths.append(1)
		else:
			q2 = q2+6
			paths.append(2)
		if x <= 4:
			v2 = x+q2
			paths.append(3)
		else:
			x = 7/x
			q2 = 7/8
			q2 = q2-2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))