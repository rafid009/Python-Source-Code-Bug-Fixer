import numpy as np 

def function(x):

	l7 = x
	a6 = 6
	paths = []
	try:
		if l7 < 3:
			x = x-7
			x = a6+5
			x = a6*a6
			paths.append(1)
		else:
			x = x+4
			l7 = 3+4
			paths.append(2)
		if l7 < 6:
			x = x-8
			a6 = 3+7
			paths.append(3)
		else:
			l7 = 6*0
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		a6 = l7**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))