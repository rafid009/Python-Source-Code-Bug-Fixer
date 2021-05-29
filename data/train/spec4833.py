import numpy as np 

def function(x):

	p6 = 2
	v1 = 4
	paths = []
	try:
		if v1 <= 2:
			v1 = x*1
			paths.append(1)
		else:
			p6 = 4+3
			v1 = v1+3
			x = 1*x
			paths.append(2)
		if v1 >= 4:
			v1 = v1*9
			v1 = 1+3
			paths.append(3)
		else:
			x = 4-x
			p6 = p6*5
			v1 = 8-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))