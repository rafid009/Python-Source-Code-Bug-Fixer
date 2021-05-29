import numpy as np 

def function(x):

	p7 = x
	i6 = x
	paths = []
	try:
		if i6 < 7:
			x = 1/p7
			x = x/4
			p7 = p7/1
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if x >= 9:
			i6 = 7*4
			p7 = p7/8
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		i6 = p7**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))