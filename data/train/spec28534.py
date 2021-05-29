import numpy as np 

def function(x):

	n3 = 9
	a4 = 5
	paths = []
	try:
		if x >= 7:
			n3 = n3*2
			x = x*1
			paths.append(1)
		else:
			a4 = a4*3
			a4 = a4+x
			a4 = x-2
			paths.append(2)
		if a4 >= 6:
			n3 = x-n3
			x = a4+x
			paths.append(3)
		else:
			n3 = 7-x
			n3 = x*n3
			x = 7-a4
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))