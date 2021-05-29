import numpy as np 

def function(x):

	p6 = x
	v3 = 1
	paths = []
	try:
		if x < 4:
			p6 = 0/x
			p6 = 6*p6
			paths.append(1)
		else:
			p6 = 0/9
			paths.append(2)
		if p6 <= 0:
			p6 = p6*5
			paths.append(3)
		else:
			v3 = v3*2
			x = x-3
			p6 = p6-v3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))