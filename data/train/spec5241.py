import numpy as np 

def function(x):

	q8 = 2
	k5 = x
	paths = []
	try:
		if q8 > 9:
			k5 = 2*0
			x = 9*k5
			x = 9-x
			paths.append(1)
		else:
			q8 = 1+q8
			paths.append(2)
		if k5 < 7:
			q8 = q8/k5
			k5 = k5/x
			k5 = 7-k5
			paths.append(3)
		else:
			q8 = q8+q8
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