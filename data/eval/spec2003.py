import numpy as np 

def function(x):

	t8 = x
	b8 = x
	paths = []
	try:
		if b8 < 1:
			x = x+0
			t8 = t8-6
			paths.append(1)
		else:
			t8 = 4+t8
			paths.append(2)
		if x <= 5:
			t8 = 8*t8
			paths.append(3)
		else:
			t8 = 9-t8
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))