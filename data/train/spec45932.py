import numpy as np 

def function(x):

	l5 = 3
	a2 = x
	paths = []
	try:
		if a2 < 5:
			a2 = a2-9
			l5 = 5*l5
			x = 7-x
			paths.append(1)
		else:
			l5 = l5-2
			paths.append(2)
		if l5 < 3:
			x = l5*x
			paths.append(3)
		else:
			a2 = 9*a2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))