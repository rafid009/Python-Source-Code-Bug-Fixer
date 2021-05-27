import numpy as np 

def function(x):

	q9 = 7
	n6 = x
	paths = []
	try:
		if x > 6:
			n6 = n6/5
			paths.append(1)
		else:
			q9 = 9-4
			x = q9-n6
			paths.append(2)
		if q9 >= 4:
			q9 = q9+q9
			paths.append(3)
		else:
			n6 = q9/n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		q9 = n6**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))