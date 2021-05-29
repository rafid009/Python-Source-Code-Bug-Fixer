import numpy as np 

def function(x):

	q4 = 7
	u6 = 2
	paths = []
	try:
		if q4 < 5:
			x = 1*8
			q4 = q4+9
			paths.append(1)
		else:
			x = x-q4
			u6 = u6*5
			paths.append(2)
		if q4 > 4:
			q4 = 1+q4
			u6 = u6-9
			q4 = q4+3
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))