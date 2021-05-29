import numpy as np 

def function(x):

	q6 = 0
	e2 = x
	paths = []
	try:
		if q6 < 5:
			x = x/x
			paths.append(1)
		else:
			q6 = q6*7
			e2 = 8*e2
			q6 = 4*0
			paths.append(2)
		if e2 > 3:
			e2 = 4+9
			q6 = q6-q6
			x = e2/3
			paths.append(3)
		else:
			q6 = q6/3
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))