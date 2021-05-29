import numpy as np 

def function(x):

	a8 = x
	l8 = x
	paths = []
	try:
		if l8 <= 0:
			x = a8+7
			paths.append(1)
		else:
			l8 = a8*3
			a8 = x/3
			paths.append(2)
		if l8 < 3:
			x = x*9
			x = x/8
			x = 0*x
			paths.append(3)
		else:
			x = l8-9
			l8 = l8-8
			x = 3*9
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		l8 = a8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))