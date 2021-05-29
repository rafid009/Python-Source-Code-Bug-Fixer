import numpy as np 

def function(x):

	q3 = 1
	i6 = 5
	paths = []
	try:
		if i6 < 8:
			q3 = q3/i6
			i6 = i6/4
			x = 1/4
			paths.append(1)
		else:
			i6 = 1/4
			i6 = i6/5
			paths.append(2)
		if x >= 5:
			x = q3+q3
			q3 = 9*q3
			paths.append(3)
		else:
			q3 = q3/1
			q3 = 9*5
			q3 = i6-q3
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