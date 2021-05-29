import numpy as np 

def function(x):

	q8 = x
	q6 = x
	paths = []
	try:
		if q8 < 3:
			q6 = q6*8
			q6 = 1/q6
			paths.append(1)
		else:
			q8 = 0/7
			paths.append(2)
		if q6 >= 4:
			q6 = q6/9
			paths.append(3)
		else:
			q6 = x+7
			q6 = q6+x
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))