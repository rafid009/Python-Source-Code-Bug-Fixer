import numpy as np 

def function(x):

	a7 = 4
	l0 = x
	paths = []
	try:
		if l0 > 7:
			l0 = a7-l0
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x < 9:
			a7 = l0-8
			paths.append(3)
		else:
			a7 = 3+a7
			l0 = l0/9
			l0 = a7+1
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