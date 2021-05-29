import numpy as np 

def function(x):

	i5 = 3
	r1 = 0
	paths = []
	try:
		if r1 <= 1:
			i5 = x-9
			paths.append(1)
		else:
			x = x/r1
			paths.append(2)
		if r1 >= 5:
			i5 = i5+i5
			paths.append(3)
		else:
			x = x-0
			r1 = x+r1
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))