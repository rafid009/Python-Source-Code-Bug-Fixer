import numpy as np 

def function(x):

	o4 = 5
	l0 = x
	paths = []
	try:
		if o4 < 7:
			l0 = o4*l0
			x = 4+8
			o4 = o4*9
			paths.append(1)
		else:
			l0 = 5-o4
			paths.append(2)
		if l0 >= 7:
			x = x/2
			paths.append(3)
		else:
			l0 = l0/3
			l0 = 1/l0
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