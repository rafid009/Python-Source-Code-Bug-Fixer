import numpy as np 

def function(x):

	t8 = 3
	l8 = x
	paths = []
	try:
		if l8 < 1:
			t8 = 8*t8
			x = x+x
			paths.append(1)
		else:
			l8 = l8/2
			t8 = t8/8
			l8 = l8/6
			paths.append(2)
		if t8 > 2:
			t8 = x+x
			paths.append(3)
		else:
			x = 4/x
			l8 = l8*9
			l8 = l8/l8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		t8 = l8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))