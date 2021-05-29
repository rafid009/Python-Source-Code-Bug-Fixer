import numpy as np 

def function(x):

	a9 = 9
	l6 = x
	x = 5
	paths = []
	try:
		if x <= 7:
			a9 = 8+a9
			x = 1+l6
			paths.append(1)
		else:
			l6 = 9-l6
			x = x+8
			paths.append(2)
		if x < 2:
			a9 = x-a9
			l6 = a9+l6
			x = a9/6
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		l6 = a9**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))