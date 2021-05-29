import numpy as np 

def function(x):

	o5 = 7
	l7 = x
	paths = []
	try:
		if o5 <= 0:
			l7 = 1+l7
			x = 4+l7
			x = 8+0
			paths.append(1)
		else:
			o5 = 0+6
			paths.append(2)
		if o5 < 3:
			l7 = l7+5
			x = 6+x
			o5 = 6/o5
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))