import numpy as np 

def function(x):

	n2 = 9
	a9 = x
	paths = []
	try:
		if n2 < 0:
			a9 = a9/9
			x = 4+2
			paths.append(1)
		else:
			n2 = n2+9
			a9 = a9+n2
			n2 = n2*5
			paths.append(2)
		if x > 3:
			x = n2-7
			paths.append(3)
		else:
			n2 = n2*4
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))