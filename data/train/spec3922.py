import numpy as np 

def function(x):

	n7 = x
	i9 = 8
	paths = []
	try:
		if i9 < 9:
			n7 = n7*2
			paths.append(1)
		else:
			i9 = i9-1
			i9 = 5/5
			i9 = 2+i9
			paths.append(2)
		if n7 <= 5:
			i9 = 9*i9
			i9 = i9+4
			x = x-6
			paths.append(3)
		else:
			n7 = n7-0
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))