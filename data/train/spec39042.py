import numpy as np 

def function(x):

	n3 = 2
	t9 = x
	paths = []
	try:
		if n3 < 0:
			t9 = n3+x
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if x > 8:
			n3 = t9+n3
			n3 = n3/t9
			x = 7*x
			paths.append(3)
		else:
			t9 = 8-n3
			t9 = t9+5
			n3 = n3-6
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