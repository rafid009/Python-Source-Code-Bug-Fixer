import numpy as np 

def function(x):

	l4 = x
	o0 = x
	paths = []
	try:
		if x > 7:
			l4 = 2/l4
			x = x*x
			o0 = 4/o0
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if o0 > 7:
			x = x-x
			o0 = o0*x
			l4 = 0/6
			paths.append(3)
		else:
			l4 = 9-l4
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))