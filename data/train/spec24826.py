import numpy as np 

def function(x):

	q6 = x
	j3 = 0
	paths = []
	try:
		if x < 0:
			q6 = 2+8
			paths.append(1)
		else:
			x = x*6
			x = x-2
			paths.append(2)
		if x < 1:
			j3 = x/6
			q6 = x*q6
			paths.append(3)
		else:
			q6 = q6+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))