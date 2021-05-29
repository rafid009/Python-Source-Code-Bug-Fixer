import numpy as np 

def function(x):

	l1 = x
	t2 = 2
	paths = []
	try:
		if l1 >= 3:
			t2 = t2/t2
			x = x/2
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x < 1:
			l1 = 2/5
			l1 = 2+l1
			x = l1-4
			paths.append(3)
		else:
			x = t2*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))