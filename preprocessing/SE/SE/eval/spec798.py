import numpy as np 

def function(x):

	l4 = 0
	o5 = 2
	paths = []
	try:
		if o5 >= 9:
			o5 = l4*1
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if o5 > 5:
			o5 = x*x
			l4 = l4*2
			paths.append(3)
		else:
			l4 = l4-2
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