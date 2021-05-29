import numpy as np 

def function(x):

	i9 = 8
	n7 = 8
	paths = []
	try:
		if i9 <= 6:
			x = x*0
			n7 = n7-i9
			paths.append(1)
		else:
			x = 5+x
			n7 = n7+8
			i9 = 5-i9
			paths.append(2)
		if n7 <= 9:
			i9 = i9/1
			n7 = 2*n7
			i9 = i9/i9
			paths.append(3)
		else:
			i9 = 2*6
			i9 = 4*i9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))