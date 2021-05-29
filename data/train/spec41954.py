import numpy as np 

def function(x):

	a9 = x
	b5 = x
	x = 2
	paths = []
	try:
		if x >= 0:
			x = a9*x
			b5 = b5/2
			paths.append(1)
		else:
			a9 = 7-4
			a9 = b5*a9
			b5 = x+1
			paths.append(2)
		if b5 >= 2:
			b5 = a9+a9
			paths.append(3)
		else:
			x = 4+6
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))