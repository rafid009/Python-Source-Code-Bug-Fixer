import numpy as np 

def function(x):

	q4 = 5
	f6 = 2
	paths = []
	try:
		if q4 > 8:
			q4 = q4/q4
			paths.append(1)
		else:
			q4 = x/q4
			paths.append(2)
		if x < 8:
			f6 = q4/f6
			q4 = f6*f6
			q4 = q4-q4
			paths.append(3)
		else:
			f6 = f6-1
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))