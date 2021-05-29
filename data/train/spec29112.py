import numpy as np 

def function(x):

	n4 = x
	v2 = x
	paths = []
	try:
		if x > 8:
			n4 = 5-n4
			n4 = 4+n4
			paths.append(1)
		else:
			n4 = 3-9
			n4 = n4*8
			n4 = n4+3
			paths.append(2)
		if v2 >= 1:
			n4 = 4*2
			n4 = n4/x
			v2 = v2*n4
			paths.append(3)
		else:
			n4 = 3*n4
			x = v2*x
			n4 = 0*n4
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		n4 = v2**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))