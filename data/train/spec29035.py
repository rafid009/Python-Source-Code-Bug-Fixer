import numpy as np 

def function(x):

	v4 = 2
	p6 = x
	paths = []
	try:
		if p6 > 3:
			p6 = 8*x
			paths.append(1)
		else:
			v4 = p6*1
			v4 = x-v4
			v4 = v4*1
			paths.append(2)
		if x <= 1:
			v4 = 5*9
			p6 = p6*7
			paths.append(3)
		else:
			x = p6-4
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))