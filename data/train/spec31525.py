import numpy as np 

def function(x):

	q8 = 8
	q6 = x
	paths = []
	try:
		if q6 <= 9:
			q8 = q6-q8
			q6 = q8+0
			q8 = q8+8
			paths.append(1)
		else:
			q8 = 2*q8
			q8 = x-q6
			q8 = 0*0
			paths.append(2)
		if q8 >= 5:
			q6 = 9-q6
			paths.append(3)
		else:
			x = x*0
			q8 = x/8
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q8 = q6**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))