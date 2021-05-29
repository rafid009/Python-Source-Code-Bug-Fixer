import numpy as np 

def function(x):

	o7 = 4
	l3 = x
	paths = []
	try:
		if o7 < 2:
			o7 = 5*x
			paths.append(1)
		else:
			x = x-2
			o7 = 4*o7
			paths.append(2)
		if o7 > 4:
			x = x+o7
			paths.append(3)
		else:
			o7 = 7-o7
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))