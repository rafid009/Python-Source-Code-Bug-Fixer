import numpy as np 

def function(x):

	i7 = x
	p3 = x
	paths = []
	try:
		if x >= 7:
			i7 = i7/4
			paths.append(1)
		else:
			p3 = 5/3
			p3 = p3/6
			i7 = i7*3
			paths.append(2)
		if x >= 8:
			x = 1*x
			x = x/i7
			paths.append(3)
		else:
			i7 = i7/x
			i7 = 1-i7
			p3 = p3-9
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