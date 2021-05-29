import numpy as np 

def function(x):

	j8 = x
	q0 = x
	paths = []
	try:
		if q0 <= 1:
			j8 = j8-q0
			j8 = j8/q0
			j8 = 7-5
			paths.append(1)
		else:
			j8 = 3/2
			q0 = q0*6
			q0 = q0/3
			paths.append(2)
		if q0 >= 6:
			x = x*3
			j8 = j8-7
			paths.append(3)
		else:
			j8 = x-1
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