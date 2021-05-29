import numpy as np 

def function(x):

	a7 = 3
	n9 = 2
	x = x
	paths = []
	try:
		if n9 >= 7:
			x = a7+x
			a7 = a7*7
			paths.append(1)
		else:
			a7 = a7-7
			paths.append(2)
		if x >= 8:
			n9 = n9/x
			x = x/5
			a7 = x-a7
			paths.append(3)
		else:
			a7 = 5+a7
			n9 = 0-n9
			x = a7-x
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		a7 = n9**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))