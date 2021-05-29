import numpy as np 

def function(x):

	n3 = x
	a7 = x
	paths = []
	try:
		if x <= 9:
			a7 = 9/6
			paths.append(1)
		else:
			a7 = x*x
			n3 = 8+8
			x = x*a7
			paths.append(2)
		if x <= 5:
			n3 = 6-9
			x = x+x
			n3 = n3-8
			paths.append(3)
		else:
			n3 = a7+3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		a7 = n3**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))