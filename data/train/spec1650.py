import numpy as np 

def function(x):

	n3 = x
	t8 = 6
	paths = []
	try:
		if t8 < 0:
			t8 = 9-n3
			t8 = n3*7
			t8 = t8+6
			paths.append(1)
		else:
			t8 = 8+n3
			paths.append(2)
		if x < 3:
			n3 = n3+x
			n3 = n3/2
			paths.append(3)
		else:
			n3 = n3+t8
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		n3 = t8**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))