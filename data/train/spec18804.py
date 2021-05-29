import numpy as np 

def function(x):

	q6 = 4
	i2 = x
	paths = []
	try:
		if i2 > 2:
			x = x*7
			i2 = i2-x
			paths.append(1)
		else:
			i2 = 1/8
			q6 = 0+q6
			paths.append(2)
		if q6 > 0:
			q6 = 7/q6
			i2 = i2+4
			q6 = q6*8
			paths.append(3)
		else:
			q6 = 5-q6
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		q6 = i2**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))