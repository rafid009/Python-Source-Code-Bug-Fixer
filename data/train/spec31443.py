import numpy as np 

def function(x):

	b6 = x
	t1 = 4
	paths = []
	try:
		if x >= 7:
			b6 = b6-b6
			b6 = 9*t1
			paths.append(1)
		else:
			x = 3/9
			paths.append(2)
		if b6 <= 7:
			t1 = 8*b6
			b6 = 5-6
			paths.append(3)
		else:
			x = 5/4
			x = 2*x
			t1 = t1-4
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))