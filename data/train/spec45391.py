import numpy as np 

def function(x):

	q4 = 0
	r1 = x
	paths = []
	try:
		if r1 <= 9:
			x = x+q4
			paths.append(1)
		else:
			q4 = 3+9
			r1 = 6/5
			x = 1/x
			paths.append(2)
		if r1 < 7:
			q4 = 2+x
			q4 = q4+9
			paths.append(3)
		else:
			r1 = 3/r1
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