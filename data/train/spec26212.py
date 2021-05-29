import numpy as np 

def function(x):

	n7 = x
	i4 = x
	paths = []
	try:
		if n7 > 9:
			i4 = n7+5
			paths.append(1)
		else:
			x = x/9
			x = x+0
			n7 = x*9
			paths.append(2)
		if i4 < 6:
			i4 = 3-0
			paths.append(3)
		else:
			i4 = i4*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))