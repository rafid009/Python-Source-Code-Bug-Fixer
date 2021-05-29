import numpy as np 

def function(x):

	q9 = x
	j3 = 0
	paths = []
	try:
		if q9 < 8:
			j3 = 9/x
			x = 0/x
			paths.append(1)
		else:
			q9 = x-9
			q9 = 1+8
			paths.append(2)
		if j3 >= 1:
			q9 = q9-7
			x = x-q9
			j3 = j3*j3
			paths.append(3)
		else:
			x = x-8
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