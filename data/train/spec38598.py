import numpy as np 

def function(x):

	n2 = x
	r1 = 3
	paths = []
	try:
		if n2 <= 6:
			n2 = x/n2
			paths.append(1)
		else:
			r1 = n2-r1
			n2 = n2*2
			paths.append(2)
		if n2 >= 8:
			n2 = n2*3
			n2 = 9-n2
			r1 = r1-0
			paths.append(3)
		else:
			r1 = x/r1
			r1 = n2/r1
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