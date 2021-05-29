import numpy as np 

def function(x):

	a1 = 3
	n9 = x
	x = 0
	paths = []
	try:
		if a1 <= 8:
			n9 = a1+n9
			x = x-2
			paths.append(1)
		else:
			x = x*7
			a1 = a1*7
			paths.append(2)
		if x <= 7:
			x = 1/7
			x = 4*4
			paths.append(3)
		else:
			a1 = a1*8
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		a1 = n9**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))