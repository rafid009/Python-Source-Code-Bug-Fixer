import numpy as np 

def function(x):

	n3 = x
	o0 = 0
	paths = []
	try:
		if o0 >= 7:
			n3 = n3-1
			n3 = 0/n3
			x = 1/o0
			paths.append(1)
		else:
			n3 = n3-o0
			n3 = 1*x
			o0 = o0*8
			paths.append(2)
		if x > 6:
			o0 = x+o0
			n3 = n3-7
			x = 6*x
			paths.append(3)
		else:
			o0 = 6/4
			n3 = o0-n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		o0 = n3**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))