import numpy as np 

def function(x):

	q3 = 6
	f7 = x
	paths = []
	try:
		if q3 > 5:
			f7 = q3*f7
			x = x+7
			paths.append(1)
		else:
			x = x-x
			f7 = 8*x
			f7 = 6*f7
			paths.append(2)
		if x <= 5:
			f7 = f7/9
			paths.append(3)
		else:
			q3 = 6-x
			f7 = f7*8
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))