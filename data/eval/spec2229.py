import numpy as np 

def function(x):

	b0 = 8
	l1 = x
	paths = []
	try:
		if b0 <= 9:
			x = l1/6
			paths.append(1)
		else:
			l1 = 6-l1
			paths.append(2)
		if x > 5:
			b0 = 9+x
			b0 = b0+5
			l1 = 7*l1
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))