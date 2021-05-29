import numpy as np 

def function(x):

	j9 = x
	q9 = 3
	paths = []
	try:
		if j9 < 0:
			q9 = q9+3
			x = q9-x
			paths.append(1)
		else:
			q9 = j9+3
			j9 = 1-6
			x = x/x
			paths.append(2)
		if q9 <= 0:
			x = x*x
			paths.append(3)
		else:
			q9 = q9-7
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))