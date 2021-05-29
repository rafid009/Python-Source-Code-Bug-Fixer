import numpy as np 

def function(x):

	p7 = 5
	n6 = x
	paths = []
	try:
		if p7 >= 2:
			x = n6-p7
			p7 = p7+x
			p7 = p7/p7
			paths.append(1)
		else:
			n6 = 7-6
			n6 = n6/n6
			paths.append(2)
		if x < 7:
			n6 = x-n6
			x = x/9
			p7 = p7-3
			paths.append(3)
		else:
			n6 = n6+1
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))