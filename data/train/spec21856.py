import numpy as np 

def function(x):

	a2 = 1
	q2 = 6
	paths = []
	try:
		if x >= 1:
			q2 = q2+8
			a2 = 3/a2
			paths.append(1)
		else:
			a2 = 3*a2
			paths.append(2)
		if q2 <= 4:
			x = 7*q2
			x = x+0
			paths.append(3)
		else:
			q2 = x*q2
			a2 = a2+2
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