import numpy as np 

def function(x):

	t2 = x
	l1 = 1
	paths = []
	try:
		if t2 > 4:
			x = t2-x
			paths.append(1)
		else:
			l1 = l1+l1
			t2 = t2-7
			paths.append(2)
		if t2 > 3:
			x = x-2
			x = 2*6
			l1 = x/l1
			paths.append(3)
		else:
			l1 = l1+l1
			l1 = 5/x
			l1 = 6*5
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))