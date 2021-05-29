import numpy as np 

def function(x):

	q6 = 6
	o2 = 7
	paths = []
	try:
		if x >= 9:
			o2 = o2-8
			paths.append(1)
		else:
			o2 = q6/o2
			q6 = x/q6
			paths.append(2)
		if x <= 9:
			o2 = o2*8
			paths.append(3)
		else:
			o2 = 1*o2
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))