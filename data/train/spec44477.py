import numpy as np 

def function(x):

	b9 = 6
	q6 = x
	paths = []
	try:
		if x > 9:
			b9 = b9/8
			x = q6-x
			paths.append(1)
		else:
			q6 = 4*q6
			x = 7-x
			b9 = q6*x
			paths.append(2)
		if b9 < 4:
			x = 2*q6
			x = 0*9
			x = b9-6
			paths.append(3)
		else:
			b9 = 3-b9
			b9 = 1+b9
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))