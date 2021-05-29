import numpy as np 

def function(x):

	t5 = x
	l7 = x
	paths = []
	try:
		if x >= 3:
			x = x-5
			paths.append(1)
		else:
			t5 = t5*8
			x = x+4
			l7 = 2*6
			paths.append(2)
		if t5 < 2:
			l7 = l7+0
			l7 = 8-l7
			t5 = t5-9
			paths.append(3)
		else:
			l7 = l7+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))