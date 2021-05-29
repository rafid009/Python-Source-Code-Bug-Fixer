import numpy as np 

def function(x):

	f7 = x
	l2 = 6
	paths = []
	try:
		if x < 7:
			l2 = l2*3
			paths.append(1)
		else:
			f7 = 1+6
			f7 = 1*f7
			paths.append(2)
		if f7 <= 1:
			x = x-x
			l2 = 3/l2
			f7 = f7-1
			paths.append(3)
		else:
			f7 = 7/5
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))