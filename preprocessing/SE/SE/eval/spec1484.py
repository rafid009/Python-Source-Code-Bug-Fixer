import numpy as np 

def function(x):

	n2 = x
	o1 = x
	paths = []
	try:
		if o1 >= 3:
			x = x-3
			n2 = n2+8
			paths.append(1)
		else:
			n2 = x/o1
			o1 = x*3
			x = x/8
			paths.append(2)
		if x <= 3:
			o1 = o1+3
			n2 = n2-x
			paths.append(3)
		else:
			o1 = o1/o1
			x = x/x
			n2 = 0-n2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		o1 = n2**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))