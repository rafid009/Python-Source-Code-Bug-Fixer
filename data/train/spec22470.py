import numpy as np 

def function(x):

	p7 = x
	i1 = 7
	paths = []
	try:
		if x <= 6:
			p7 = 6-7
			x = p7*x
			paths.append(1)
		else:
			i1 = i1/1
			paths.append(2)
		if p7 > 1:
			x = x/2
			paths.append(3)
		else:
			x = x+1
			p7 = p7/6
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))