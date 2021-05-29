import numpy as np 

def function(x):

	i4 = 1
	l3 = x
	paths = []
	try:
		if l3 >= 2:
			x = 7*x
			paths.append(1)
		else:
			i4 = 0+l3
			paths.append(2)
		if i4 < 9:
			i4 = i4*4
			l3 = 4-4
			paths.append(3)
		else:
			l3 = x/2
			i4 = 1+i4
			i4 = 5*i4
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