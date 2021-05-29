import numpy as np 

def function(x):

	l2 = x
	o0 = 6
	x = 6
	paths = []
	try:
		if l2 >= 8:
			l2 = 1*l2
			paths.append(1)
		else:
			x = l2*x
			l2 = l2-6
			o0 = o0-9
			paths.append(2)
		if x > 8:
			l2 = l2-0
			x = l2*x
			x = x+l2
			paths.append(3)
		else:
			x = x*x
			l2 = o0/l2
			x = 0*6
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		o0 = l2**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))