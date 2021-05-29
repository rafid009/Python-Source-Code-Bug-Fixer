import numpy as np 

def function(x):

	t2 = x
	l2 = x
	paths = []
	try:
		if l2 <= 8:
			x = 1-x
			paths.append(1)
		else:
			l2 = l2*l2
			x = t2+x
			x = x/2
			paths.append(2)
		if x < 7:
			l2 = l2-t2
			x = l2-x
			t2 = 3+5
			paths.append(3)
		else:
			t2 = l2-x
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x = l2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))