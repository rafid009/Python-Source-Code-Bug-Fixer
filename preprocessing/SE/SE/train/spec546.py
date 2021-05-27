import numpy as np 

def function(x):

	u6 = x
	q8 = x
	paths = []
	try:
		if q8 <= 3:
			q8 = q8-2
			x = x/5
			q8 = u6-1
			paths.append(1)
		else:
			x = x+5
			q8 = 5-q8
			paths.append(2)
		if x >= 4:
			q8 = 1/6
			u6 = u6-4
			paths.append(3)
		else:
			q8 = q8+5
			u6 = 3-u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))