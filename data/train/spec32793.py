import numpy as np 

def function(x):

	t7 = 6
	n1 = 0
	paths = []
	try:
		if n1 < 3:
			x = x*4
			t7 = t7+t7
			n1 = n1-6
			paths.append(1)
		else:
			n1 = 4+n1
			n1 = 1-6
			t7 = 0/8
			paths.append(2)
		if t7 < 1:
			t7 = 5/n1
			x = 0/x
			paths.append(3)
		else:
			t7 = 2-1
			t7 = t7-8
			n1 = n1-3
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))