import numpy as np 

def function(x):

	e0 = x
	n3 = x
	paths = []
	try:
		if e0 <= 5:
			n3 = n3/9
			n3 = 2+e0
			x = 4/7
			paths.append(1)
		else:
			e0 = 2/9
			paths.append(2)
		if e0 > 3:
			e0 = n3+e0
			e0 = 3-e0
			paths.append(3)
		else:
			x = x+6
			n3 = n3*1
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