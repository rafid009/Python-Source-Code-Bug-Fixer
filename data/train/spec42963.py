import numpy as np 

def function(x):

	p7 = 4
	i6 = x
	paths = []
	try:
		if p7 < 7:
			x = x+p7
			p7 = 8+p7
			i6 = i6*6
			paths.append(1)
		else:
			p7 = p7/p7
			p7 = 9*x
			paths.append(2)
		if p7 >= 5:
			p7 = p7*8
			p7 = i6/p7
			paths.append(3)
		else:
			p7 = 3-p7
			i6 = 0/2
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))