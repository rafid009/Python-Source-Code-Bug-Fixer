import numpy as np 

def function(x):

	a2 = x
	n4 = x
	paths = []
	try:
		if n4 >= 3:
			x = 3*8
			paths.append(1)
		else:
			x = a2/6
			a2 = 6-n4
			n4 = 7-n4
			paths.append(2)
		if n4 > 8:
			a2 = a2+9
			n4 = n4+5
			paths.append(3)
		else:
			a2 = 6-a2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))