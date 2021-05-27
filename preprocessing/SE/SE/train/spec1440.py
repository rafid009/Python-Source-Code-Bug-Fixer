import numpy as np 

def function(x):

	a0 = 8
	l4 = 3
	paths = []
	try:
		if x < 0:
			l4 = x*5
			l4 = 4+l4
			paths.append(1)
		else:
			l4 = a0/3
			paths.append(2)
		if a0 <= 7:
			x = x*0
			a0 = a0+2
			paths.append(3)
		else:
			l4 = l4-a0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))