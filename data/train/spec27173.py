import numpy as np 

def function(x):

	p2 = 6
	i7 = x
	paths = []
	try:
		if i7 >= 9:
			i7 = i7/9
			paths.append(1)
		else:
			x = 3/x
			x = 2*i7
			i7 = p2*p2
			paths.append(2)
		if x >= 2:
			i7 = 2+i7
			i7 = p2*3
			paths.append(3)
		else:
			i7 = x-i7
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))