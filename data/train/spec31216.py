import numpy as np 

def function(x):

	j9 = x
	n9 = x
	paths = []
	try:
		if x <= 9:
			x = x*2
			paths.append(1)
		else:
			j9 = 2/n9
			paths.append(2)
		if j9 >= 4:
			x = x/x
			j9 = 1*2
			paths.append(3)
		else:
			j9 = n9/j9
			n9 = n9+j9
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