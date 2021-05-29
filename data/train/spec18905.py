import numpy as np 

def function(x):

	u9 = 3
	q8 = x
	paths = []
	try:
		if u9 >= 8:
			x = x*5
			x = 0/6
			paths.append(1)
		else:
			u9 = u9/5
			paths.append(2)
		if q8 >= 0:
			q8 = q8-8
			u9 = 6-q8
			q8 = q8*6
			paths.append(3)
		else:
			u9 = u9/2
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))