import numpy as np 

def function(x):

	f2 = 2
	l1 = x
	paths = []
	try:
		if l1 < 1:
			f2 = 1*f2
			paths.append(1)
		else:
			f2 = f2+l1
			x = x*5
			l1 = l1+5
			paths.append(2)
		if l1 > 7:
			l1 = 8/2
			l1 = x-7
			paths.append(3)
		else:
			x = x+f2
			l1 = l1*3
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