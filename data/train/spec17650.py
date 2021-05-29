import numpy as np 

def function(x):

	q9 = x
	v7 = x
	paths = []
	try:
		if x < 7:
			v7 = q9-v7
			paths.append(1)
		else:
			x = x-q9
			x = x+x
			q9 = q9+v7
			paths.append(2)
		if q9 <= 6:
			v7 = v7+2
			v7 = 9+v7
			paths.append(3)
		else:
			v7 = 3+v7
			q9 = 1+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))