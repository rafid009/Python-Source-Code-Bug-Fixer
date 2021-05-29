import numpy as np 

def function(x):

	l7 = x
	o6 = 6
	paths = []
	try:
		if l7 >= 7:
			x = 2+l7
			o6 = 5/7
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if o6 > 6:
			l7 = 9/2
			x = 5*x
			x = 1+x
			paths.append(3)
		else:
			o6 = 5-o6
			o6 = 0-8
			x = l7-x
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		l7 = o6**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))