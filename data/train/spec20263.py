import numpy as np 

def function(x):

	o9 = x
	l4 = x
	paths = []
	try:
		if o9 > 3:
			o9 = 4*o9
			x = l4+1
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if o9 <= 6:
			o9 = o9/x
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))