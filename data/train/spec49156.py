import numpy as np 

def function(x):

	t5 = x
	l8 = x
	paths = []
	try:
		if l8 >= 1:
			t5 = 7*t5
			paths.append(1)
		else:
			t5 = t5-1
			t5 = 8/5
			l8 = l8/5
			paths.append(2)
		if t5 < 3:
			t5 = t5+x
			x = x+1
			l8 = 6/l8
			paths.append(3)
		else:
			t5 = t5+x
			t5 = t5*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))