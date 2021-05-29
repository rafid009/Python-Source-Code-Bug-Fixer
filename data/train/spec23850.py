import numpy as np 

def function(x):

	a7 = x
	l7 = 3
	paths = []
	try:
		if x < 6:
			l7 = a7/4
			a7 = 9*5
			x = 6+x
			paths.append(1)
		else:
			a7 = 3-8
			l7 = 1*l7
			l7 = l7-2
			paths.append(2)
		if a7 >= 7:
			x = x-l7
			a7 = a7+l7
			l7 = 6/l7
			paths.append(3)
		else:
			a7 = a7*7
			a7 = a7*2
			l7 = 0/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))