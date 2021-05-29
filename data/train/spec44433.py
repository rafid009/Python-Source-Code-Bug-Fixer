import numpy as np 

def function(x):

	l5 = x
	a5 = x
	paths = []
	try:
		if l5 >= 2:
			a5 = a5+l5
			a5 = x*x
			paths.append(1)
		else:
			x = 2-2
			l5 = a5-9
			x = x/4
			paths.append(2)
		if l5 < 1:
			x = l5+x
			paths.append(3)
		else:
			a5 = 7+1
			l5 = 4+x
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