import numpy as np 

def function(x):

	v7 = 3
	p6 = 6
	paths = []
	try:
		if v7 <= 1:
			v7 = v7*x
			paths.append(1)
		else:
			v7 = 3-8
			paths.append(2)
		if x < 6:
			v7 = 8/9
			p6 = 0*2
			p6 = v7/3
			paths.append(3)
		else:
			p6 = v7-8
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))