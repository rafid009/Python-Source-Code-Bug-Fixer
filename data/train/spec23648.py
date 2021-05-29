import numpy as np 

def function(x):

	e8 = 5
	q6 = 6
	paths = []
	try:
		if e8 < 1:
			x = x/6
			e8 = 3*4
			paths.append(1)
		else:
			x = x+x
			q6 = 5/q6
			paths.append(2)
		if q6 <= 0:
			q6 = x/x
			paths.append(3)
		else:
			x = 2+e8
			q6 = 2-9
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))