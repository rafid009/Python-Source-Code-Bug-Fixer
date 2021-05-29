import numpy as np 

def function(x):

	e1 = x
	n9 = x
	paths = []
	try:
		if n9 >= 2:
			e1 = e1-5
			e1 = 0/n9
			paths.append(1)
		else:
			n9 = x+5
			x = x/4
			x = n9*x
			paths.append(2)
		if e1 > 5:
			e1 = e1*x
			e1 = 6-n9
			n9 = n9*n9
			paths.append(3)
		else:
			x = 8-6
			x = x/n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))