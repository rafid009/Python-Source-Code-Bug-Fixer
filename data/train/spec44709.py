import numpy as np 

def function(x):

	o0 = x
	l7 = 5
	paths = []
	try:
		if o0 > 1:
			l7 = o0+9
			paths.append(1)
		else:
			l7 = 7/8
			o0 = o0-0
			x = 6*x
			paths.append(2)
		if l7 >= 0:
			l7 = l7+x
			x = 8-x
			x = 0-3
			paths.append(3)
		else:
			l7 = x-x
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		l7 = o0**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))