import numpy as np 

def function(x):

	b5 = 4
	l9 = x
	x = x
	paths = []
	try:
		if x < 1:
			x = x+2
			paths.append(1)
		else:
			b5 = 2+b5
			x = x-7
			paths.append(2)
		if b5 > 4:
			x = 9*l9
			paths.append(3)
		else:
			b5 = b5-5
			b5 = 2+4
			l9 = l9*b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))