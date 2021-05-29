import numpy as np 

def function(x):

	p3 = 6
	i4 = 9
	paths = []
	try:
		if x > 7:
			i4 = 3*i4
			paths.append(1)
		else:
			p3 = 4-p3
			i4 = x+4
			paths.append(2)
		if i4 > 5:
			p3 = p3/2
			p3 = 6/8
			x = x-i4
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))