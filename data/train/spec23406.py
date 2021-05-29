import numpy as np 

def function(x):

	l5 = 7
	a3 = 2
	paths = []
	try:
		if x <= 7:
			a3 = 4/a3
			paths.append(1)
		else:
			x = x/x
			l5 = 9/l5
			paths.append(2)
		if x > 5:
			x = 0*x
			paths.append(3)
		else:
			a3 = a3*0
			l5 = 5+l5
			a3 = a3+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))