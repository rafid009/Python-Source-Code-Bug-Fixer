import numpy as np 

def function(x):

	n9 = x
	j5 = 5
	paths = []
	try:
		if n9 >= 7:
			n9 = n9*n9
			paths.append(1)
		else:
			n9 = n9-8
			j5 = 7-4
			paths.append(2)
		if n9 <= 3:
			j5 = x*j5
			j5 = j5*8
			x = j5*x
			paths.append(3)
		else:
			x = x*x
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