import numpy as np 

def function(x):

	n2 = 3
	o9 = x
	paths = []
	try:
		if x < 8:
			n2 = 5*n2
			paths.append(1)
		else:
			x = 3+x
			x = x*7
			x = 5*x
			paths.append(2)
		if x > 6:
			o9 = x*1
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		n2 = o9**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))