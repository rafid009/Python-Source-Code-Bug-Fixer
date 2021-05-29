import numpy as np 

def function(x):

	q3 = 2
	n5 = x
	paths = []
	try:
		if q3 <= 5:
			n5 = n5-1
			x = q3-x
			q3 = x*q3
			paths.append(1)
		else:
			x = n5*x
			x = x*8
			paths.append(2)
		if q3 <= 7:
			q3 = n5*q3
			paths.append(3)
		else:
			x = 1/x
			n5 = n5-9
			q3 = q3/2
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		q3 = n5**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))