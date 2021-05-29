import numpy as np 

def function(x):

	o5 = x
	l5 = 0
	paths = []
	try:
		if o5 < 1:
			l5 = l5+x
			l5 = x/6
			paths.append(1)
		else:
			l5 = l5+4
			l5 = l5/8
			paths.append(2)
		if x >= 5:
			o5 = o5*o5
			l5 = o5-l5
			x = l5-o5
			paths.append(3)
		else:
			o5 = 1-l5
			l5 = l5/5
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