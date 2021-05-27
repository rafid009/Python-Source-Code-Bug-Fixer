import numpy as np 

def function(x):

	n2 = 1
	t7 = x
	paths = []
	try:
		if n2 > 6:
			n2 = 7/n2
			n2 = t7/x
			paths.append(1)
		else:
			t7 = x+t7
			t7 = t7*5
			t7 = t7*6
			paths.append(2)
		if n2 <= 0:
			t7 = t7+3
			paths.append(3)
		else:
			n2 = n2+t7
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))