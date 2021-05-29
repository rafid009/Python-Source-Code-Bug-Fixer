import numpy as np 

def function(x):

	v1 = x
	p7 = x
	paths = []
	try:
		if x >= 4:
			x = v1/p7
			x = p7+x
			paths.append(1)
		else:
			v1 = 1*v1
			v1 = 7/9
			p7 = p7/9
			paths.append(2)
		if x >= 1:
			v1 = 8+v1
			x = 4+x
			paths.append(3)
		else:
			x = 3*p7
			v1 = p7+v1
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		v1 = p7**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))