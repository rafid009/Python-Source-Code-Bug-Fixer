import numpy as np 

def function(x):

	q3 = x
	l3 = 8
	x = 1
	paths = []
	try:
		if q3 < 1:
			l3 = l3/3
			paths.append(1)
		else:
			l3 = l3-3
			q3 = q3+x
			paths.append(2)
		if x >= 3:
			q3 = 4/q3
			paths.append(3)
		else:
			l3 = l3-q3
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