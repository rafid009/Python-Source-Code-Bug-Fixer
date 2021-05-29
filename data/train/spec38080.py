import numpy as np 

def function(x):

	l2 = x
	t9 = x
	paths = []
	try:
		if x <= 8:
			l2 = l2/8
			x = l2+x
			paths.append(1)
		else:
			l2 = l2*5
			l2 = l2/2
			t9 = t9/8
			paths.append(2)
		if x >= 6:
			x = l2/6
			x = 7+x
			x = 6-x
			paths.append(3)
		else:
			l2 = 1*l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		t9 = l2**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))