import numpy as np 

def function(x):

	o4 = 3
	l1 = 2
	paths = []
	try:
		if x >= 1:
			x = x*2
			paths.append(1)
		else:
			x = x/6
			l1 = x-7
			x = 3-x
			paths.append(2)
		if o4 <= 6:
			x = x+x
			paths.append(3)
		else:
			x = o4-x
			x = x*6
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		o4 = l1**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))