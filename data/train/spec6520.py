import numpy as np 

def function(x):

	l8 = x
	t8 = x
	paths = []
	try:
		if t8 < 8:
			x = 3/x
			x = x/9
			x = 3-6
			paths.append(1)
		else:
			t8 = x-x
			x = x-l8
			l8 = 1*1
			paths.append(2)
		if l8 < 0:
			t8 = l8-t8
			x = x+x
			t8 = t8*t8
			paths.append(3)
		else:
			t8 = l8/9
			t8 = t8-9
			l8 = 6-l8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))