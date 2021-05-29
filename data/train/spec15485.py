import numpy as np 

def function(x):

	n3 = x
	i3 = 0
	paths = []
	try:
		if n3 >= 2:
			n3 = 1*n3
			n3 = 2/n3
			i3 = 2+6
			paths.append(1)
		else:
			i3 = i3-n3
			n3 = x/x
			n3 = 3+n3
			paths.append(2)
		if x < 6:
			i3 = 4*i3
			paths.append(3)
		else:
			n3 = 2-n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))