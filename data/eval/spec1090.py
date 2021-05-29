import numpy as np 

def function(x):

	q8 = 5
	u7 = 4
	paths = []
	try:
		if u7 > 1:
			x = u7+8
			paths.append(1)
		else:
			q8 = q8+8
			x = q8*3
			u7 = u7+x
			paths.append(2)
		if x >= 6:
			q8 = u7-4
			u7 = u7-0
			q8 = 2-3
			paths.append(3)
		else:
			u7 = 1*u7
			u7 = q8+x
			u7 = 6-x
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))