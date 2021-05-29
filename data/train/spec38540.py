import numpy as np 

def function(x):

	l3 = 5
	l6 = x
	paths = []
	try:
		if l3 > 1:
			l3 = 0/5
			x = x+l6
			paths.append(1)
		else:
			l3 = 9+2
			l3 = 9*7
			paths.append(2)
		if l6 >= 5:
			l6 = l6*4
			l3 = x*l3
			x = 4/x
			paths.append(3)
		else:
			x = l3+x
			l6 = l6+2
			x = l3-l6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))