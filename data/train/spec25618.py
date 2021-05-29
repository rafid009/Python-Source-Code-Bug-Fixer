import numpy as np 

def function(x):

	l5 = 7
	n7 = x
	paths = []
	try:
		if x < 3:
			l5 = 0-l5
			l5 = n7-6
			paths.append(1)
		else:
			l5 = l5+7
			x = 4/x
			paths.append(2)
		if n7 <= 5:
			n7 = 9*n7
			l5 = x-4
			n7 = x-n7
			paths.append(3)
		else:
			n7 = 1*n7
			x = l5-8
			l5 = n7/5
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		l5 = n7**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))