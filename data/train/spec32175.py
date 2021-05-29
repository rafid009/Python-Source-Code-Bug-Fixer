import numpy as np 

def function(x):

	t2 = 6
	n3 = x
	paths = []
	try:
		if x < 8:
			x = t2+n3
			x = x*9
			x = t2/7
			paths.append(1)
		else:
			t2 = 1*x
			paths.append(2)
		if n3 > 0:
			n3 = x-4
			x = n3/x
			paths.append(3)
		else:
			t2 = t2+x
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