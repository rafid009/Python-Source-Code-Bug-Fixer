import numpy as np 

def function(x):

	p7 = 9
	v1 = 9
	paths = []
	try:
		if v1 < 0:
			v1 = v1*1
			p7 = p7+v1
			v1 = p7+7
			paths.append(1)
		else:
			v1 = v1*6
			x = 9*x
			p7 = v1+x
			paths.append(2)
		if v1 <= 0:
			v1 = 9-8
			v1 = v1/v1
			p7 = 8-3
			paths.append(3)
		else:
			p7 = 2-x
			v1 = 5+v1
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