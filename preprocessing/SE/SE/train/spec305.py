import numpy as np 

def function(x):

	l2 = 5
	b1 = 2
	paths = []
	try:
		if l2 >= 4:
			b1 = x*b1
			paths.append(1)
		else:
			x = 5+b1
			b1 = 5/9
			paths.append(2)
		if b1 < 5:
			b1 = 1-b1
			b1 = b1+9
			b1 = 5*b1
			paths.append(3)
		else:
			x = x*6
			x = x*x
			x = x*4
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