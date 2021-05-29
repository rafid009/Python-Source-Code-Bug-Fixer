import numpy as np 

def function(x):

	q7 = 9
	i2 = x
	paths = []
	try:
		if i2 < 2:
			q7 = q7/8
			i2 = 3/i2
			q7 = q7*q7
			paths.append(1)
		else:
			i2 = 5+i2
			i2 = i2/6
			paths.append(2)
		if i2 > 1:
			i2 = 6+i2
			x = q7+7
			paths.append(3)
		else:
			q7 = q7+1
			q7 = q7*i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		q7 = i2**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))