import numpy as np 

def function(x):

	n3 = x
	e3 = 0
	paths = []
	try:
		if n3 > 4:
			e3 = 2+x
			n3 = e3*x
			paths.append(1)
		else:
			x = n3/3
			paths.append(2)
		if e3 >= 8:
			n3 = n3*n3
			e3 = 7+5
			paths.append(3)
		else:
			x = x/4
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