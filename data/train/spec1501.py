import numpy as np 

def function(x):

	o6 = 2
	l4 = 8
	x = x
	paths = []
	try:
		if o6 > 4:
			x = 8/1
			o6 = 3+o6
			paths.append(1)
		else:
			l4 = l4+x
			o6 = x+o6
			paths.append(2)
		if x <= 2:
			o6 = o6+5
			l4 = 0+1
			paths.append(3)
		else:
			o6 = 4/o6
			o6 = o6*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))