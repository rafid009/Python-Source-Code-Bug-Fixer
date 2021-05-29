import numpy as np 

def function(x):

	x3 = x
	q6 = x
	paths = []
	try:
		if x <= 0:
			x = q6*x
			x = x-1
			paths.append(1)
		else:
			q6 = x+2
			x = x3*9
			paths.append(2)
		if x3 < 4:
			x = 5+x
			q6 = 3*8
			x = x*q6
			paths.append(3)
		else:
			x = q6+2
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		q6 = x3**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))