import numpy as np 

def function(x):

	t2 = 6
	n2 = x
	paths = []
	try:
		if x >= 3:
			n2 = n2-4
			paths.append(1)
		else:
			t2 = t2/n2
			paths.append(2)
		if x <= 5:
			x = x*3
			n2 = n2*5
			x = 1/x
			paths.append(3)
		else:
			n2 = n2-x
			n2 = 4*n2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))