import numpy as np 

def function(x):

	x3 = 4
	i1 = 8
	paths = []
	try:
		if x3 < 5:
			i1 = i1+x3
			paths.append(1)
		else:
			x3 = x3+x
			i1 = i1*4
			paths.append(2)
		if i1 < 4:
			i1 = i1/4
			x = 5-2
			i1 = i1+i1
			paths.append(3)
		else:
			i1 = i1-1
			x = i1*0
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))