import numpy as np 

def function(x):

	x6 = 3
	n2 = x
	x = x
	paths = []
	try:
		if n2 <= 1:
			x6 = x6+n2
			n2 = 5/n2
			paths.append(1)
		else:
			x6 = 5+7
			x = x6+3
			n2 = n2*8
			paths.append(2)
		if n2 < 2:
			x6 = x6+n2
			paths.append(3)
		else:
			n2 = n2*n2
			n2 = n2+x6
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))