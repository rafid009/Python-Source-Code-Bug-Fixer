import numpy as np 

def function(x):

	k4 = 5
	q2 = x
	paths = []
	try:
		if q2 > 1:
			q2 = q2+q2
			k4 = 0-6
			q2 = 5+5
			paths.append(1)
		else:
			q2 = x+q2
			paths.append(2)
		if q2 >= 7:
			q2 = 0-q2
			k4 = k4+k4
			paths.append(3)
		else:
			k4 = 8-0
			q2 = q2*3
			q2 = q2*4
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