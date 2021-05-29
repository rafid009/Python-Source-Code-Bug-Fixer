import numpy as np 

def function(x):

	p6 = 7
	v2 = 9
	x = x
	paths = []
	try:
		if x < 0:
			x = p6*x
			paths.append(1)
		else:
			v2 = 5/v2
			p6 = 7-v2
			x = 9/x
			paths.append(2)
		if p6 >= 5:
			p6 = x/x
			p6 = p6-9
			paths.append(3)
		else:
			p6 = p6*1
			v2 = 1+v2
			v2 = v2+v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))