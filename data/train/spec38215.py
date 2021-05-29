import numpy as np 

def function(x):

	n3 = x
	e0 = 9
	x = x
	paths = []
	try:
		if x >= 4:
			e0 = e0/7
			x = 5/4
			x = x+n3
			paths.append(1)
		else:
			x = x*5
			n3 = n3/9
			x = x+e0
			paths.append(2)
		if e0 < 0:
			n3 = n3*0
			paths.append(3)
		else:
			x = n3*n3
			n3 = n3-x
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))