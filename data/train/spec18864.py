import numpy as np 

def function(x):

	l0 = x
	o5 = x
	paths = []
	try:
		if l0 < 2:
			x = o5*x
			paths.append(1)
		else:
			o5 = o5/1
			x = x*o5
			x = 7-l0
			paths.append(2)
		if l0 <= 6:
			o5 = 2*x
			paths.append(3)
		else:
			o5 = x+5
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))