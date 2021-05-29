import numpy as np 

def function(x):

	n1 = x
	i6 = x
	paths = []
	try:
		if n1 > 2:
			x = 9-i6
			x = 4+7
			x = x*2
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if n1 < 1:
			x = 4*x
			n1 = n1/n1
			paths.append(3)
		else:
			i6 = x/n1
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		n1 = i6**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))