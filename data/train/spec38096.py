import numpy as np 

def function(x):

	j3 = 7
	q6 = 3
	paths = []
	try:
		if q6 >= 1:
			j3 = j3-2
			q6 = q6*j3
			paths.append(1)
		else:
			j3 = j3/8
			q6 = q6-3
			x = j3+9
			paths.append(2)
		if x > 7:
			x = 6+x
			j3 = 1-j3
			x = 8-x
			paths.append(3)
		else:
			q6 = 2/j3
			q6 = 5/q6
			j3 = 7/j3
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