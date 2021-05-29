import numpy as np 

def function(x):

	p6 = x
	i0 = 6
	x = x
	paths = []
	try:
		if i0 >= 6:
			x = i0-i0
			i0 = i0/6
			paths.append(1)
		else:
			x = x*i0
			p6 = x*p6
			x = 0/x
			paths.append(2)
		if x >= 5:
			i0 = i0*5
			paths.append(3)
		else:
			p6 = p6-5
			i0 = 2/8
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		i0 = p6**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))