import numpy as np 

def function(x):

	r5 = x
	l7 = x
	paths = []
	try:
		if x >= 1:
			r5 = x*7
			l7 = 8/9
			paths.append(1)
		else:
			r5 = l7/8
			x = l7/1
			x = x-8
			paths.append(2)
		if x > 6:
			x = 3*0
			r5 = x-9
			paths.append(3)
		else:
			l7 = 9*l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))