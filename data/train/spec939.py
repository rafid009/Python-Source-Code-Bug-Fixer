import numpy as np 

def function(x):

	t5 = 7
	b2 = x
	paths = []
	try:
		if x >= 8:
			x = 9*x
			x = t5+8
			b2 = x*t5
			paths.append(1)
		else:
			b2 = 2+b2
			t5 = t5-3
			paths.append(2)
		if x <= 1:
			b2 = 3+b2
			t5 = t5-4
			paths.append(3)
		else:
			t5 = t5*6
			x = 8-x
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		t5 = b2**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))