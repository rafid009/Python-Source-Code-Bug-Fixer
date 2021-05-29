import numpy as np 

def function(x):

	l5 = x
	x6 = 2
	paths = []
	try:
		if l5 <= 2:
			x = x*8
			paths.append(1)
		else:
			x6 = x6*6
			l5 = 0-l5
			paths.append(2)
		if x6 <= 5:
			l5 = l5*4
			paths.append(3)
		else:
			x6 = x6/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))