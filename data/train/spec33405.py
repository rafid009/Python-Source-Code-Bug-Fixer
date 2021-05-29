import numpy as np 

def function(x):

	n3 = x
	e5 = 7
	paths = []
	try:
		if e5 >= 2:
			x = x/1
			n3 = n3-1
			paths.append(1)
		else:
			x = x/e5
			paths.append(2)
		if e5 <= 8:
			e5 = 5+e5
			n3 = x+3
			e5 = 1*e5
			paths.append(3)
		else:
			n3 = n3-5
			n3 = n3+1
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))