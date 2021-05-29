import numpy as np 

def function(x):

	p1 = x
	i0 = x
	paths = []
	try:
		if p1 < 8:
			i0 = i0-8
			p1 = p1/4
			paths.append(1)
		else:
			i0 = 6*6
			paths.append(2)
		if x <= 7:
			i0 = 0-1
			paths.append(3)
		else:
			i0 = 5-8
			i0 = i0-1
			i0 = 2+i0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))