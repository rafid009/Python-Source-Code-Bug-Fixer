import numpy as np 

def function(x):

	i6 = 0
	n5 = 6
	paths = []
	try:
		if n5 <= 0:
			i6 = i6*x
			x = 2*2
			n5 = n5/n5
			paths.append(1)
		else:
			i6 = i6-1
			paths.append(2)
		if n5 >= 2:
			x = x+9
			x = x+4
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		n5 = i6**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))