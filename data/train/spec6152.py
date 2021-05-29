import numpy as np 

def function(x):

	r3 = 0
	l2 = 3
	paths = []
	try:
		if x < 6:
			r3 = x-9
			paths.append(1)
		else:
			l2 = l2/x
			paths.append(2)
		if r3 <= 9:
			x = 4/2
			x = r3+x
			l2 = r3/x
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))