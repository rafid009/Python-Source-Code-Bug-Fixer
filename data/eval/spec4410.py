import numpy as np 

def function(x):

	z7 = 8
	l5 = x
	paths = []
	try:
		if x < 4:
			l5 = 5*1
			z7 = x/5
			x = 0+6
			paths.append(1)
		else:
			x = z7-l5
			x = x/5
			paths.append(2)
		if l5 <= 2:
			x = 5*x
			l5 = 1+l5
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		l5 = z7**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))