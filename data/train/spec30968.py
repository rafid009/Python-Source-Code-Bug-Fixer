import numpy as np 

def function(x):

	l7 = x
	o4 = 4
	paths = []
	try:
		if o4 >= 1:
			x = o4/6
			x = x-l7
			o4 = x+0
			paths.append(1)
		else:
			l7 = 8*1
			l7 = l7+4
			x = x*3
			paths.append(2)
		if l7 <= 2:
			x = 3/x
			x = 5/5
			paths.append(3)
		else:
			x = x-l7
			o4 = o4-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))