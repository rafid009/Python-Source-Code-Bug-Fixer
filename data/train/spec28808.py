import numpy as np 

def function(x):

	u6 = x
	q8 = x
	x = x
	paths = []
	try:
		if x > 3:
			q8 = q8*u6
			u6 = u6-u6
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if x > 5:
			u6 = u6+q8
			q8 = q8+0
			paths.append(3)
		else:
			x = q8-7
			x = q8/q8
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