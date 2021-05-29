import numpy as np 

def function(x):

	o5 = x
	l4 = 3
	x = 2
	paths = []
	try:
		if o5 > 2:
			l4 = 2+l4
			x = x/x
			o5 = 5+x
			paths.append(1)
		else:
			o5 = o5*1
			paths.append(2)
		if x >= 5:
			o5 = o5*1
			o5 = 7/2
			l4 = l4+l4
			paths.append(3)
		else:
			o5 = 3-o5
			o5 = o5/2
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))