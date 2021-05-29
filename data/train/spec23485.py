import numpy as np 

def function(x):

	b0 = 2
	q3 = 7
	paths = []
	try:
		if q3 >= 6:
			q3 = 5-q3
			paths.append(1)
		else:
			x = 5/b0
			q3 = q3+8
			paths.append(2)
		if x > 4:
			q3 = b0/q3
			q3 = q3+1
			paths.append(3)
		else:
			q3 = q3-x
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		b0 = q3**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))