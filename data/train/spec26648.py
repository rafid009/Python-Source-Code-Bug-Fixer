import numpy as np 

def function(x):

	l9 = 1
	a6 = x
	x = x
	paths = []
	try:
		if x >= 4:
			l9 = 9+a6
			paths.append(1)
		else:
			l9 = l9+5
			l9 = a6+4
			paths.append(2)
		if l9 >= 9:
			a6 = 3-a6
			l9 = l9-2
			l9 = l9*l9
			paths.append(3)
		else:
			x = 8+a6
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))