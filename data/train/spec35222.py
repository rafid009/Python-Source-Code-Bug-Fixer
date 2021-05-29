import numpy as np 

def function(x):

	o0 = 7
	a1 = x
	x = x
	paths = []
	try:
		if o0 <= 5:
			a1 = a1*8
			paths.append(1)
		else:
			o0 = o0-a1
			paths.append(2)
		if o0 > 8:
			a1 = a1/3
			paths.append(3)
		else:
			o0 = o0+x
			o0 = a1*5
			a1 = a1/o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))