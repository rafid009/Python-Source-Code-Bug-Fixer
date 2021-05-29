import numpy as np 

def function(x):

	f0 = 5
	l2 = 8
	paths = []
	try:
		if l2 <= 3:
			f0 = 4/f0
			l2 = f0+l2
			f0 = x+1
			paths.append(1)
		else:
			f0 = 8-8
			l2 = l2+x
			paths.append(2)
		if x > 9:
			x = 0-2
			l2 = 0+4
			paths.append(3)
		else:
			x = f0*x
			l2 = 4*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))