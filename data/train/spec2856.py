import numpy as np 

def function(x):

	n2 = 3
	j1 = 8
	paths = []
	try:
		if j1 <= 2:
			n2 = n2/n2
			paths.append(1)
		else:
			j1 = j1*1
			n2 = 5/x
			paths.append(2)
		if n2 <= 6:
			n2 = 8*n2
			x = x+n2
			n2 = 7+x
			paths.append(3)
		else:
			x = x+j1
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