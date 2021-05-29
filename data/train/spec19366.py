import numpy as np 

def function(x):

	a3 = x
	l9 = x
	paths = []
	try:
		if l9 <= 0:
			x = 4*l9
			x = x-2
			paths.append(1)
		else:
			l9 = l9+5
			x = 4-l9
			paths.append(2)
		if l9 <= 0:
			a3 = a3-5
			paths.append(3)
		else:
			l9 = l9-5
			l9 = l9*0
			l9 = 5*3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))