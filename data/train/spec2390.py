import numpy as np 

def function(x):

	n7 = x
	v3 = 1
	paths = []
	try:
		if x <= 2:
			n7 = 5-n7
			n7 = 1*9
			paths.append(1)
		else:
			v3 = v3/n7
			paths.append(2)
		if n7 < 6:
			x = n7+x
			paths.append(3)
		else:
			x = v3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))