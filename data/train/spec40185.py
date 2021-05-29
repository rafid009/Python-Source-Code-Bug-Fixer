import numpy as np 

def function(x):

	n1 = 1
	t7 = x
	paths = []
	try:
		if t7 <= 6:
			n1 = n1+x
			paths.append(1)
		else:
			t7 = x-4
			n1 = t7/n1
			paths.append(2)
		if n1 >= 2:
			x = x*x
			t7 = t7-t7
			paths.append(3)
		else:
			t7 = x*x
			t7 = 0-x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		t7 = n1**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))