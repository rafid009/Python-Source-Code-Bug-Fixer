import numpy as np 

def function(x):

	b4 = x
	n2 = 7
	paths = []
	try:
		if n2 > 5:
			n2 = 6*x
			n2 = 8-x
			paths.append(1)
		else:
			n2 = n2-0
			paths.append(2)
		if x >= 8:
			n2 = 7/n2
			paths.append(3)
		else:
			n2 = b4/3
			b4 = 0*x
			n2 = b4+n2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		b4 = n2**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))