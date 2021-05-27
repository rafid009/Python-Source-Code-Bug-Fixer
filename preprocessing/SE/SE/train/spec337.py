import numpy as np 

def function(x):

	f8 = 1
	n1 = 3
	paths = []
	try:
		if f8 > 4:
			n1 = n1+n1
			paths.append(1)
		else:
			n1 = n1/9
			paths.append(2)
		if f8 <= 9:
			n1 = n1/6
			paths.append(3)
		else:
			n1 = n1*f8
			f8 = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))