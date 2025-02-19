import numpy as np 

def function(x):

	q5 = x
	j0 = 3
	paths = []
	try:
		if q5 <= 1:
			q5 = q5/5
			paths.append(1)
		else:
			j0 = 7/3
			paths.append(2)
		if q5 <= 2:
			j0 = j0-q5
			x = q5+5
			paths.append(3)
		else:
			q5 = 4+q5
			j0 = 1+j0
			q5 = 3+q5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))