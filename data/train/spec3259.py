import numpy as np 

def function(x):

	o5 = x
	o2 = 4
	paths = []
	try:
		if o5 <= 2:
			o2 = o2*x
			o5 = o5+o2
			o2 = 4-o5
			paths.append(1)
		else:
			x = 8*0
			paths.append(2)
		if x >= 2:
			o5 = 5+4
			o2 = 1*o2
			paths.append(3)
		else:
			o5 = 2+o5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))