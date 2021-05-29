import numpy as np 

def function(x):

	w2 = 1
	i1 = 9
	paths = []
	try:
		if i1 >= 4:
			w2 = 1-2
			paths.append(1)
		else:
			w2 = w2+x
			paths.append(2)
		if x >= 5:
			i1 = 6-2
			x = i1/w2
			paths.append(3)
		else:
			x = 1-1
			x = 0*8
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