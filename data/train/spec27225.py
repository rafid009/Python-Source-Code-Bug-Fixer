import numpy as np 

def function(x):

	o0 = x
	o1 = 2
	paths = []
	try:
		if x > 3:
			o1 = o1/7
			paths.append(1)
		else:
			o1 = o0*4
			paths.append(2)
		if x >= 4:
			o1 = o1*4
			o1 = 2+x
			paths.append(3)
		else:
			x = 1-2
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o0 = o1**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))