import numpy as np 

def function(x):

	n9 = x
	c2 = x
	paths = []
	try:
		if c2 < 4:
			n9 = c2*n9
			paths.append(1)
		else:
			x = c2*x
			x = 7+x
			paths.append(2)
		if x > 9:
			x = 5/n9
			paths.append(3)
		else:
			x = x*n9
			n9 = 5+c2
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