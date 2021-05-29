import numpy as np 

def function(x):

	n4 = x
	i1 = x
	x = 9
	paths = []
	try:
		if i1 >= 3:
			x = x+5
			x = i1-n4
			x = i1-x
			paths.append(1)
		else:
			x = x-5
			x = 2/7
			paths.append(2)
		if i1 <= 5:
			x = 8+i1
			i1 = 4-0
			paths.append(3)
		else:
			i1 = i1*n4
			x = 0+x
			n4 = 4/n4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))