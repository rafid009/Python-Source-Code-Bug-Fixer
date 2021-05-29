import numpy as np 

def function(x):

	l7 = 8
	a9 = 4
	paths = []
	try:
		if x >= 3:
			x = a9-x
			x = 4*l7
			l7 = a9-3
			paths.append(1)
		else:
			x = a9+x
			l7 = 7/8
			l7 = 6/l7
			paths.append(2)
		if x >= 6:
			l7 = a9*0
			a9 = 2-5
			paths.append(3)
		else:
			l7 = 6*0
			l7 = l7*l7
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		l7 = a9**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))