import numpy as np 

def function(x):

	b2 = x
	l5 = 9
	paths = []
	try:
		if l5 >= 1:
			x = 2-3
			paths.append(1)
		else:
			x = 6*b2
			paths.append(2)
		if b2 > 6:
			b2 = 3-l5
			paths.append(3)
		else:
			b2 = b2+7
			b2 = 1/b2
			l5 = 5*l5
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		l5 = b2**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))