import numpy as np 

def function(x):

	q1 = x
	v6 = 8
	paths = []
	try:
		if q1 > 2:
			v6 = v6-9
			q1 = 4/q1
			paths.append(1)
		else:
			v6 = v6*4
			x = q1/4
			paths.append(2)
		if v6 < 3:
			x = 4-x
			paths.append(3)
		else:
			x = x*q1
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		q1 = v6**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))