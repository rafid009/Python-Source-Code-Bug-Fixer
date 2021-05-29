import numpy as np 

def function(x):

	n9 = 3
	t7 = 5
	paths = []
	try:
		if t7 >= 6:
			t7 = t7/4
			n9 = n9/n9
			paths.append(1)
		else:
			n9 = n9-4
			t7 = 9/x
			t7 = t7+x
			paths.append(2)
		if t7 >= 0:
			x = x/x
			x = 1/6
			t7 = 2+x
			paths.append(3)
		else:
			x = x-1
			x = 3*x
			n9 = n9+6
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		n9 = t7**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))