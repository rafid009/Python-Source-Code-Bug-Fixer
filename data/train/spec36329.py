import numpy as np 

def function(x):

	a7 = x
	n1 = x
	paths = []
	try:
		if n1 < 2:
			x = x+a7
			x = n1*5
			x = n1/3
			paths.append(1)
		else:
			n1 = x-3
			paths.append(2)
		if x > 8:
			x = x+x
			n1 = x-8
			paths.append(3)
		else:
			x = 2+4
			x = x-2
			x = x*a7
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))