import numpy as np 

def function(x):

	b4 = x
	l2 = x
	paths = []
	try:
		if l2 >= 8:
			x = l2*x
			l2 = 5*l2
			paths.append(1)
		else:
			x = b4/9
			paths.append(2)
		if l2 <= 5:
			x = x*4
			l2 = l2/x
			paths.append(3)
		else:
			b4 = b4+7
			x = x+6
			l2 = l2*l2
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