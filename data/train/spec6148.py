import numpy as np 

def function(x):

	q8 = 3
	v1 = x
	x = x
	paths = []
	try:
		if x >= 3:
			v1 = x-v1
			paths.append(1)
		else:
			x = q8/x
			x = x+x
			q8 = 5-x
			paths.append(2)
		if v1 < 0:
			q8 = q8+x
			x = v1/x
			paths.append(3)
		else:
			x = 8+7
			v1 = v1*1
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))