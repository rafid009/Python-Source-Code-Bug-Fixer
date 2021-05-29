import numpy as np 

def function(x):

	l5 = 5
	a0 = 1
	paths = []
	try:
		if x >= 9:
			x = 9+3
			l5 = a0/l5
			paths.append(1)
		else:
			l5 = l5*l5
			paths.append(2)
		if a0 <= 4:
			l5 = l5-a0
			x = x/4
			a0 = 9+a0
			paths.append(3)
		else:
			l5 = l5*2
			x = 9*x
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