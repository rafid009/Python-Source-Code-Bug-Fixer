import numpy as np 

def function(x):

	o0 = 3
	f0 = x
	paths = []
	try:
		if f0 < 4:
			x = x+4
			x = 1+7
			o0 = 5/o0
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if o0 < 7:
			x = 9-x
			x = 3+x
			paths.append(3)
		else:
			f0 = x+1
			x = 9/x
			f0 = f0+8
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