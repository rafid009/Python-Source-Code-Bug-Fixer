import numpy as np 

def function(x):

	n3 = 7
	i6 = x
	paths = []
	try:
		if i6 < 7:
			i6 = 0-i6
			x = x-1
			i6 = 0+i6
			paths.append(1)
		else:
			i6 = i6-7
			paths.append(2)
		if n3 >= 6:
			i6 = 4-4
			n3 = n3+6
			i6 = i6*2
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