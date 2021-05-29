import numpy as np 

def function(x):

	l3 = 0
	o0 = 7
	paths = []
	try:
		if x <= 8:
			x = x+4
			l3 = l3-l3
			o0 = 5/o0
			paths.append(1)
		else:
			o0 = l3+9
			paths.append(2)
		if o0 >= 2:
			x = x+x
			paths.append(3)
		else:
			x = o0/x
			o0 = l3*4
			o0 = 9+o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))