import numpy as np 

def function(x):

	l5 = 2
	q1 = x
	x = 7
	paths = []
	try:
		if l5 >= 6:
			q1 = q1-l5
			paths.append(1)
		else:
			l5 = 1/5
			l5 = 0*6
			paths.append(2)
		if l5 >= 0:
			x = 1-x
			x = 4*1
			paths.append(3)
		else:
			l5 = 5+7
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))