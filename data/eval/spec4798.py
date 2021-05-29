import numpy as np 

def function(x):

	q5 = 0
	f9 = x
	paths = []
	try:
		if q5 > 1:
			q5 = 5/4
			paths.append(1)
		else:
			q5 = q5+3
			paths.append(2)
		if x < 4:
			f9 = f9/f9
			f9 = 8-6
			q5 = f9-q5
			paths.append(3)
		else:
			f9 = 9+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))