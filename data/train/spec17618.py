import numpy as np 

def function(x):

	o5 = 9
	n3 = 1
	paths = []
	try:
		if x < 5:
			n3 = 8+n3
			n3 = n3+2
			o5 = n3-o5
			paths.append(1)
		else:
			n3 = 9*1
			n3 = 2/o5
			n3 = n3-8
			paths.append(2)
		if o5 >= 7:
			o5 = 4-o5
			x = 4+o5
			o5 = 2+2
			paths.append(3)
		else:
			o5 = 2/n3
			x = 9/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))