import numpy as np 

def function(x):

	l9 = 0
	i8 = 6
	paths = []
	try:
		if x < 2:
			i8 = i8+4
			paths.append(1)
		else:
			i8 = i8+i8
			i8 = i8/5
			x = 6+x
			paths.append(2)
		if x <= 8:
			x = x*3
			l9 = l9+5
			l9 = i8/7
			paths.append(3)
		else:
			i8 = i8+4
			x = 6*i8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))