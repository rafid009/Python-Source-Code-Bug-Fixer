import numpy as np 

def function(x):

	o5 = x
	l5 = x
	paths = []
	try:
		if l5 >= 2:
			l5 = x-o5
			paths.append(1)
		else:
			x = 0-o5
			x = x/8
			paths.append(2)
		if l5 > 5:
			l5 = l5+5
			paths.append(3)
		else:
			o5 = 7*3
			x = l5+x
			x = x*5
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