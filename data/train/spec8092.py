import numpy as np 

def function(x):

	l9 = 5
	o1 = 2
	paths = []
	try:
		if o1 < 9:
			x = x/4
			x = x*9
			l9 = o1*x
			paths.append(1)
		else:
			x = o1+o1
			o1 = o1+1
			paths.append(2)
		if l9 > 5:
			x = 1+x
			x = 7/l9
			x = x-8
			paths.append(3)
		else:
			l9 = 2/l9
			x = 5*x
			x = 6*x
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