import numpy as np 

def function(x):

	i4 = 6
	p4 = 0
	paths = []
	try:
		if x <= 9:
			i4 = 4+i4
			paths.append(1)
		else:
			x = 6*8
			paths.append(2)
		if i4 < 4:
			x = x+5
			paths.append(3)
		else:
			p4 = 2*x
			p4 = i4+0
			p4 = p4*i4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))