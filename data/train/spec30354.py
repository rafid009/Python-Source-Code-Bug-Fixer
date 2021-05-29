import numpy as np 

def function(x):

	l7 = x
	o7 = 5
	x = x
	paths = []
	try:
		if x >= 9:
			l7 = l7/4
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if l7 > 4:
			o7 = o7/2
			o7 = l7*o7
			paths.append(3)
		else:
			x = x*2
			o7 = o7-8
			l7 = l7*4
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