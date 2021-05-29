import numpy as np 

def function(x):

	o7 = x
	l5 = x
	x = x
	paths = []
	try:
		if o7 > 7:
			o7 = o7+9
			paths.append(1)
		else:
			x = 9+x
			o7 = 2+3
			paths.append(2)
		if l5 >= 0:
			x = 0+x
			x = 3+x
			paths.append(3)
		else:
			l5 = l5+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))