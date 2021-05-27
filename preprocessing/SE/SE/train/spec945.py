import numpy as np 

def function(x):

	i1 = x
	r6 = 1
	x = x
	paths = []
	try:
		if r6 < 2:
			i1 = i1-1
			paths.append(1)
		else:
			x = x/1
			r6 = 6*4
			i1 = x*8
			paths.append(2)
		if i1 < 5:
			x = x+x
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))