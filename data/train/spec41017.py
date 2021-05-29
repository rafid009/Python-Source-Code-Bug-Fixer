import numpy as np 

def function(x):

	l3 = x
	o4 = x
	paths = []
	try:
		if o4 >= 7:
			l3 = l3/5
			x = 0-x
			paths.append(1)
		else:
			x = x*0
			l3 = o4*o4
			paths.append(2)
		if x < 3:
			x = x/l3
			paths.append(3)
		else:
			o4 = o4*o4
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