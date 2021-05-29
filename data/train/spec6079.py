import numpy as np 

def function(x):

	n9 = x
	o0 = 6
	paths = []
	try:
		if n9 >= 0:
			o0 = 6-o0
			n9 = x-n9
			paths.append(1)
		else:
			o0 = x*o0
			paths.append(2)
		if n9 >= 9:
			x = o0+x
			paths.append(3)
		else:
			o0 = 3+o0
			n9 = x+9
			x = o0*n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))