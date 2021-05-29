import numpy as np 

def function(x):

	q0 = x
	i4 = 6
	x = 7
	paths = []
	try:
		if q0 > 2:
			i4 = i4-x
			i4 = i4/6
			i4 = i4+i4
			paths.append(1)
		else:
			q0 = q0+0
			q0 = 0-q0
			q0 = 6-i4
			paths.append(2)
		if x < 4:
			x = x+9
			i4 = i4/8
			paths.append(3)
		else:
			q0 = q0*4
			q0 = q0-5
			x = x-8
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