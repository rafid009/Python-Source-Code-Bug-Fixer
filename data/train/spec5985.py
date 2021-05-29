import numpy as np 

def function(x):

	j3 = x
	n4 = 2
	paths = []
	try:
		if n4 < 2:
			x = 7+x
			x = x+1
			paths.append(1)
		else:
			j3 = 5-j3
			x = 4-x
			paths.append(2)
		if x < 6:
			j3 = j3/4
			x = x*j3
			paths.append(3)
		else:
			n4 = 6/8
			j3 = 8/j3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))