import numpy as np 

def function(x):

	i7 = x
	n3 = x
	x = x
	paths = []
	try:
		if n3 >= 5:
			x = x*6
			paths.append(1)
		else:
			n3 = n3-7
			paths.append(2)
		if i7 >= 8:
			x = 6+5
			i7 = i7-7
			paths.append(3)
		else:
			i7 = i7+2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		n3 = i7**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))