import numpy as np 

def function(x):

	z9 = x
	l2 = x
	paths = []
	try:
		if x < 2:
			x = x+9
			x = l2+l2
			x = x-7
			paths.append(1)
		else:
			l2 = x-l2
			x = 7/x
			paths.append(2)
		if z9 < 3:
			x = x/x
			x = x*1
			paths.append(3)
		else:
			l2 = 0*z9
			x = 8/4
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