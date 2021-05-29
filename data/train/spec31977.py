import numpy as np 

def function(x):

	e9 = 1
	q6 = x
	paths = []
	try:
		if e9 > 0:
			e9 = 9-2
			q6 = q6/e9
			e9 = q6+0
			paths.append(1)
		else:
			x = x+x
			e9 = e9-7
			paths.append(2)
		if q6 < 2:
			q6 = 5/3
			paths.append(3)
		else:
			q6 = x/9
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))