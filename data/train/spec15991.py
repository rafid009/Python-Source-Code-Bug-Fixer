import numpy as np 

def function(x):

	b4 = 0
	t5 = x
	paths = []
	try:
		if t5 >= 9:
			x = x+7
			paths.append(1)
		else:
			t5 = t5+4
			b4 = b4-1
			b4 = t5+b4
			paths.append(2)
		if t5 < 9:
			x = 6/b4
			t5 = t5/7
			b4 = b4-t5
			paths.append(3)
		else:
			t5 = 7+0
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))