import numpy as np 

def function(x):

	q3 = 9
	x7 = x
	paths = []
	try:
		if x7 < 5:
			q3 = q3+x7
			paths.append(1)
		else:
			q3 = q3-0
			q3 = 5+q3
			paths.append(2)
		if q3 > 5:
			q3 = q3*x
			x = x/5
			paths.append(3)
		else:
			q3 = x7*q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x7 = q3**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))