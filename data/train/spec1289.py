import numpy as np 

def function(x):

	t1 = x
	n3 = x
	x = 9
	paths = []
	try:
		if x >= 9:
			t1 = 7/n3
			t1 = n3+5
			paths.append(1)
		else:
			n3 = t1+n3
			paths.append(2)
		if t1 <= 1:
			t1 = n3-t1
			paths.append(3)
		else:
			x = n3/4
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