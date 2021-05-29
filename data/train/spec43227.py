import numpy as np 

def function(x):

	l4 = 8
	t5 = 1
	x = x
	paths = []
	try:
		if x >= 6:
			t5 = t5/1
			paths.append(1)
		else:
			t5 = 6-t5
			paths.append(2)
		if t5 <= 7:
			l4 = l4/t5
			paths.append(3)
		else:
			t5 = l4+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))