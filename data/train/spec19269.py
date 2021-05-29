import numpy as np 

def function(x):

	n2 = x
	n9 = 9
	x = 0
	paths = []
	try:
		if x >= 4:
			n2 = 5/n2
			n9 = 2/n9
			paths.append(1)
		else:
			x = 5*5
			x = 2-x
			n9 = 7*1
			paths.append(2)
		if n2 <= 3:
			n9 = n9-9
			n2 = n2/n2
			n2 = x/n2
			paths.append(3)
		else:
			n9 = 4+n2
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