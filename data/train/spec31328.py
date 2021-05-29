import numpy as np 

def function(x):

	n2 = 4
	e1 = x
	paths = []
	try:
		if x <= 8:
			x = 7+x
			n2 = x*n2
			paths.append(1)
		else:
			e1 = e1/3
			x = x*9
			n2 = 7/n2
			paths.append(2)
		if e1 >= 4:
			x = x-x
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))