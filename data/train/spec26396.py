import numpy as np 

def function(x):

	l2 = x
	o9 = 6
	paths = []
	try:
		if o9 <= 3:
			o9 = o9/o9
			o9 = x/8
			paths.append(1)
		else:
			x = 8-l2
			l2 = x/l2
			o9 = 9*o9
			paths.append(2)
		if o9 < 7:
			l2 = l2-7
			o9 = x-8
			paths.append(3)
		else:
			l2 = l2*5
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x = l2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))