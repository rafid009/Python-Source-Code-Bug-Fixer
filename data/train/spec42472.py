import numpy as np 

def function(x):

	o9 = x
	n2 = 2
	paths = []
	try:
		if o9 >= 0:
			x = 0+x
			n2 = n2*0
			n2 = n2-7
			paths.append(1)
		else:
			n2 = 0-6
			n2 = 0-x
			paths.append(2)
		if n2 <= 1:
			n2 = n2-2
			x = 2+3
			paths.append(3)
		else:
			n2 = n2/o9
			x = n2*x
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		o9 = n2**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))