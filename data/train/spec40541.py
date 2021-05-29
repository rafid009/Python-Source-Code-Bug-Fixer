import numpy as np 

def function(x):

	n1 = 2
	t3 = x
	paths = []
	try:
		if x >= 5:
			n1 = n1/x
			n1 = n1-1
			paths.append(1)
		else:
			n1 = n1-5
			x = 9-x
			n1 = n1-9
			paths.append(2)
		if n1 >= 6:
			t3 = t3+t3
			paths.append(3)
		else:
			t3 = 4-1
			n1 = 4-8
			t3 = 4/1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		t3 = n1**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))