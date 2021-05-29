import numpy as np 

def function(x):

	o5 = 8
	l2 = 7
	paths = []
	try:
		if l2 < 9:
			o5 = 7/o5
			paths.append(1)
		else:
			o5 = 5*o5
			paths.append(2)
		if x >= 6:
			o5 = o5*o5
			x = x/l2
			paths.append(3)
		else:
			l2 = l2*9
			o5 = o5/l2
			l2 = l2+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))