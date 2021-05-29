import numpy as np 

def function(x):

	x9 = 2
	q4 = x
	paths = []
	try:
		if x <= 1:
			x = x*3
			x = x-x9
			paths.append(1)
		else:
			q4 = 2+q4
			q4 = 4*8
			x = x*1
			paths.append(2)
		if q4 > 0:
			q4 = 2+7
			x9 = q4/3
			q4 = q4-2
			paths.append(3)
		else:
			x = x9/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))