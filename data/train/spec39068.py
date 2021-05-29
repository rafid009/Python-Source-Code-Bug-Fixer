import numpy as np 

def function(x):

	o5 = 9
	l2 = 5
	paths = []
	try:
		if l2 >= 3:
			x = 6/x
			x = o5*x
			o5 = o5/7
			paths.append(1)
		else:
			x = x/l2
			l2 = 3+7
			paths.append(2)
		if x <= 7:
			o5 = o5-7
			x = 2*x
			o5 = 0/o5
			paths.append(3)
		else:
			x = x/8
			l2 = l2/l2
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