import numpy as np 

def function(x):

	l7 = 2
	f7 = x
	paths = []
	try:
		if f7 <= 3:
			f7 = f7+x
			f7 = l7-x
			paths.append(1)
		else:
			l7 = l7+7
			l7 = l7+f7
			paths.append(2)
		if x < 7:
			f7 = 6/f7
			f7 = f7/f7
			paths.append(3)
		else:
			x = 4+x
			x = l7/1
			f7 = f7/7
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