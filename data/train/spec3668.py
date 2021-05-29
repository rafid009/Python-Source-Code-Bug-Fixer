import numpy as np 

def function(x):

	p6 = 3
	o5 = 2
	x = 1
	paths = []
	try:
		if p6 <= 0:
			x = 9+4
			o5 = o5*x
			paths.append(1)
		else:
			o5 = o5-8
			paths.append(2)
		if o5 < 1:
			o5 = o5/3
			paths.append(3)
		else:
			o5 = o5-p6
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))