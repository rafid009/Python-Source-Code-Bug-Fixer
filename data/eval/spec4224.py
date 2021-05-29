import numpy as np 

def function(x):

	a0 = 9
	l5 = 0
	paths = []
	try:
		if a0 <= 6:
			l5 = 8/l5
			x = x*2
			l5 = a0+a0
			paths.append(1)
		else:
			x = a0+x
			l5 = l5-8
			x = l5*x
			paths.append(2)
		if l5 > 6:
			l5 = 9-x
			l5 = 4-l5
			paths.append(3)
		else:
			x = x-7
			l5 = 8+l5
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))