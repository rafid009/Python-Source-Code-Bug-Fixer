import numpy as np 

def function(x):

	i9 = x
	p6 = x
	paths = []
	try:
		if x >= 0:
			i9 = 3*i9
			p6 = p6-6
			paths.append(1)
		else:
			i9 = i9-p6
			p6 = 8+p6
			p6 = 7-i9
			paths.append(2)
		if x > 4:
			i9 = 2-p6
			x = x-5
			p6 = p6/p6
			paths.append(3)
		else:
			p6 = 1-p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		i9 = p6**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))