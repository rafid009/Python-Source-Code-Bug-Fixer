import numpy as np 

def function(x):

	f0 = x
	l2 = x
	paths = []
	try:
		if f0 <= 8:
			l2 = l2/l2
			paths.append(1)
		else:
			f0 = 4-4
			paths.append(2)
		if x < 6:
			f0 = x+f0
			paths.append(3)
		else:
			x = 8*6
			f0 = f0*5
			l2 = 9-2
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		l2 = f0**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))