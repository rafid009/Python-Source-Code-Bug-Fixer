import numpy as np 

def function(x):

	b4 = 7
	l2 = 5
	paths = []
	try:
		if x <= 7:
			x = x/6
			x = l2*x
			paths.append(1)
		else:
			x = 2/b4
			x = 7-1
			paths.append(2)
		if x > 2:
			b4 = 8-b4
			x = x-7
			b4 = b4+8
			paths.append(3)
		else:
			b4 = l2+b4
			x = x/l2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))