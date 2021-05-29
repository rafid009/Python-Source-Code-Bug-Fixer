import numpy as np 

def function(x):

	n1 = x
	f2 = 0
	paths = []
	try:
		if n1 > 3:
			f2 = n1+n1
			f2 = f2*8
			paths.append(1)
		else:
			f2 = f2*1
			f2 = n1/x
			x = 1/x
			paths.append(2)
		if f2 >= 1:
			f2 = 4+f2
			x = x+4
			f2 = f2*f2
			paths.append(3)
		else:
			n1 = x-n1
			f2 = 2*4
			f2 = f2-6
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))