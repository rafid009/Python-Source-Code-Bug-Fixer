import numpy as np 

def function(x):

	n1 = x
	o9 = x
	paths = []
	try:
		if n1 < 4:
			x = 1*2
			paths.append(1)
		else:
			n1 = 2-7
			paths.append(2)
		if o9 >= 7:
			o9 = o9-o9
			paths.append(3)
		else:
			n1 = n1+6
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))