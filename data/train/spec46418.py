import numpy as np 

def function(x):

	p7 = x
	n9 = x
	paths = []
	try:
		if x <= 8:
			p7 = 8*2
			paths.append(1)
		else:
			p7 = 9-p7
			paths.append(2)
		if x <= 3:
			x = n9/x
			x = x+p7
			x = 6+7
			paths.append(3)
		else:
			p7 = p7/4
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		n9 = p7**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))