import numpy as np 

def function(x):

	n7 = x
	e5 = x
	paths = []
	try:
		if n7 >= 7:
			x = 1+x
			x = 1/x
			e5 = 0+e5
			paths.append(1)
		else:
			e5 = 3-e5
			n7 = n7-2
			paths.append(2)
		if e5 <= 1:
			n7 = 3+0
			n7 = n7+e5
			paths.append(3)
		else:
			x = 3/3
			n7 = 9/8
			n7 = e5/n7
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))