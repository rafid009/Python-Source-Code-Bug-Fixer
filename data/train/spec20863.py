import numpy as np 

def function(x):

	e4 = x
	n5 = 7
	paths = []
	try:
		if e4 > 4:
			e4 = 0*7
			x = x+e4
			paths.append(1)
		else:
			x = 5/e4
			n5 = e4/n5
			paths.append(2)
		if n5 > 2:
			x = 8+x
			n5 = n5/9
			e4 = 0*0
			paths.append(3)
		else:
			e4 = e4-e4
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))