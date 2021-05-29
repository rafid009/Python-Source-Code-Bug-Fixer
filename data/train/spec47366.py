import numpy as np 

def function(x):

	m2 = 1
	t9 = x
	paths = []
	try:
		if x >= 7:
			m2 = t9/3
			paths.append(1)
		else:
			t9 = 1/t9
			t9 = 1/8
			m2 = x-2
			paths.append(2)
		if m2 > 2:
			t9 = m2/8
			t9 = 7-5
			paths.append(3)
		else:
			x = 5/x
			t9 = t9*x
			m2 = m2-t9
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))