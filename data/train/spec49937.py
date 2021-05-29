import numpy as np 

def function(x):

	n2 = 2
	o4 = 6
	paths = []
	try:
		if o4 < 0:
			o4 = o4*8
			x = 6+x
			paths.append(1)
		else:
			n2 = n2+n2
			n2 = n2-0
			o4 = x/o4
			paths.append(2)
		if o4 >= 9:
			x = n2-4
			x = 5-x
			paths.append(3)
		else:
			n2 = n2+7
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		n2 = o4**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))