import numpy as np 

def function(x):

	x6 = 4
	n5 = 3
	paths = []
	try:
		if x6 > 1:
			x = 5-x
			n5 = n5-1
			x6 = x6*2
			paths.append(1)
		else:
			n5 = 0+9
			paths.append(2)
		if x6 >= 2:
			n5 = 4/x
			x = x*8
			paths.append(3)
		else:
			n5 = 7*n5
			n5 = n5+1
			x = x+x6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))