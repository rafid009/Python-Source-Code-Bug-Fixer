import numpy as np 

def function(x):

	f1 = 8
	n4 = x
	paths = []
	try:
		if n4 > 8:
			n4 = 8*6
			n4 = n4+3
			n4 = n4+5
			paths.append(1)
		else:
			x = x+9
			f1 = 0*f1
			paths.append(2)
		if x >= 6:
			x = x/2
			x = x+2
			n4 = 9*n4
			paths.append(3)
		else:
			f1 = 4+0
			f1 = f1-4
			f1 = f1*8
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		f1 = n4**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))