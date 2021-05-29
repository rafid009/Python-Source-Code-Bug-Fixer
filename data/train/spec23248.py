import numpy as np 

def function(x):

	t9 = 1
	b5 = 1
	paths = []
	try:
		if x > 7:
			b5 = b5/b5
			b5 = x*6
			paths.append(1)
		else:
			b5 = b5-6
			x = 5+x
			x = x+9
			paths.append(2)
		if x <= 9:
			b5 = b5/7
			paths.append(3)
		else:
			x = t9*1
			t9 = 2/t9
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))