import numpy as np 

def function(x):

	f4 = 1
	q6 = 5
	paths = []
	try:
		if q6 >= 0:
			f4 = 7+7
			x = x-8
			f4 = x*x
			paths.append(1)
		else:
			f4 = f4+5
			paths.append(2)
		if q6 > 6:
			f4 = f4+0
			x = x-3
			f4 = 5+f4
			paths.append(3)
		else:
			q6 = 4-q6
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