import numpy as np 

def function(x):

	t4 = x
	l8 = 3
	x = 5
	paths = []
	try:
		if x >= 9:
			x = x*t4
			paths.append(1)
		else:
			l8 = 2+t4
			paths.append(2)
		if t4 >= 8:
			x = 7/t4
			t4 = t4*9
			x = x*x
			paths.append(3)
		else:
			x = t4*5
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))