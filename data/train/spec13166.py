import numpy as np 

def function(x):

	a2 = x
	l6 = x
	paths = []
	try:
		if a2 > 3:
			l6 = l6+1
			paths.append(1)
		else:
			l6 = l6*4
			l6 = x*0
			a2 = a2/8
			paths.append(2)
		if l6 < 8:
			x = x+6
			paths.append(3)
		else:
			l6 = 9*a2
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))