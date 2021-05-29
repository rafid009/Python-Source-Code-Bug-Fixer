import numpy as np 

def function(x):

	n9 = x
	o9 = x
	paths = []
	try:
		if o9 >= 0:
			x = 6-x
			o9 = n9/n9
			n9 = n9*6
			paths.append(1)
		else:
			o9 = o9-8
			x = 6/2
			x = 0+x
			paths.append(2)
		if o9 >= 9:
			n9 = x*4
			o9 = 0*4
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))