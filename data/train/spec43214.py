import numpy as np 

def function(x):

	i6 = 6
	n7 = x
	paths = []
	try:
		if i6 > 3:
			n7 = n7/4
			x = i6-9
			paths.append(1)
		else:
			i6 = i6+x
			i6 = i6/n7
			paths.append(2)
		if n7 < 7:
			i6 = x+0
			i6 = i6*7
			paths.append(3)
		else:
			x = 2*x
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))