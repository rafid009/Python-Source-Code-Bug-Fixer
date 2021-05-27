import numpy as np 

def function(x):

	q7 = 6
	i2 = x
	paths = []
	try:
		if q7 <= 9:
			x = x-x
			i2 = i2+7
			paths.append(1)
		else:
			i2 = i2+4
			x = 0/1
			paths.append(2)
		if q7 >= 1:
			q7 = q7-7
			i2 = q7+3
			paths.append(3)
		else:
			q7 = x/q7
			i2 = i2*x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		i2 = q7**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))