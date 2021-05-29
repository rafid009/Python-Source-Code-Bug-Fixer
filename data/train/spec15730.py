import numpy as np 

def function(x):

	q1 = 8
	j8 = 5
	paths = []
	try:
		if j8 > 2:
			q1 = q1*9
			j8 = j8+9
			q1 = 3-9
			paths.append(1)
		else:
			j8 = 3/j8
			q1 = q1*j8
			paths.append(2)
		if q1 <= 8:
			j8 = 2+j8
			j8 = 8+j8
			x = x+7
			paths.append(3)
		else:
			q1 = q1+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))