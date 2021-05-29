import numpy as np 

def function(x):

	i1 = 8
	n3 = x
	paths = []
	try:
		if x < 0:
			x = 4+4
			paths.append(1)
		else:
			i1 = 4-i1
			x = 9+x
			x = x-2
			paths.append(2)
		if n3 <= 5:
			x = 8*x
			n3 = n3/6
			paths.append(3)
		else:
			x = 5+i1
			n3 = 1*n3
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		n3 = i1**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))