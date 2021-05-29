import numpy as np 

def function(x):

	b6 = 1
	o0 = x
	paths = []
	try:
		if x >= 5:
			o0 = b6*o0
			b6 = 7+b6
			paths.append(1)
		else:
			x = x*o0
			b6 = x*x
			paths.append(2)
		if o0 <= 4:
			o0 = o0*x
			x = 4-o0
			paths.append(3)
		else:
			x = o0/x
			o0 = 8*o0
			x = x+o0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))