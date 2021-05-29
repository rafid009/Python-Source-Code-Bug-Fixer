import numpy as np 

def function(x):

	l5 = x
	a8 = 8
	x = x
	paths = []
	try:
		if x > 4:
			x = x+2
			a8 = a8+2
			l5 = 0+x
			paths.append(1)
		else:
			a8 = 5+a8
			paths.append(2)
		if a8 >= 4:
			x = 1-l5
			a8 = a8/6
			paths.append(3)
		else:
			l5 = 4+7
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		a8 = l5**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))