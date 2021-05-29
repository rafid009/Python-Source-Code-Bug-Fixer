import numpy as np 

def function(x):

	l0 = x
	f2 = x
	paths = []
	try:
		if f2 >= 0:
			l0 = 9-l0
			paths.append(1)
		else:
			x = x*l0
			x = x/6
			paths.append(2)
		if f2 <= 2:
			f2 = l0-3
			x = 1*f2
			paths.append(3)
		else:
			l0 = l0+x
			x = x-1
			x = x-2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		l0 = f2**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))