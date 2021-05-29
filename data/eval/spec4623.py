import numpy as np 

def function(x):

	e6 = x
	q6 = x
	paths = []
	try:
		if e6 < 5:
			x = x/9
			e6 = x+3
			paths.append(1)
		else:
			e6 = 3/x
			e6 = x/8
			paths.append(2)
		if q6 <= 8:
			q6 = q6-4
			q6 = 8*q6
			e6 = e6-e6
			paths.append(3)
		else:
			q6 = 4-q6
			x = x/5
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))