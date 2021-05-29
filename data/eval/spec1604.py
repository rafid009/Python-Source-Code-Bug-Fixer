import numpy as np 

def function(x):

	a5 = x
	b8 = 8
	paths = []
	try:
		if b8 >= 3:
			a5 = 9+a5
			a5 = a5/x
			paths.append(1)
		else:
			a5 = b8-4
			a5 = a5/x
			a5 = a5*2
			paths.append(2)
		if b8 > 1:
			x = 6*x
			paths.append(3)
		else:
			b8 = b8/3
			b8 = b8-0
			x = 4*a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		b8 = a5**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))