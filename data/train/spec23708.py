import numpy as np 

def function(x):

	m1 = 0
	t5 = x
	paths = []
	try:
		if x >= 1:
			x = 0/x
			t5 = 9-t5
			t5 = 0*7
			paths.append(1)
		else:
			t5 = 1-x
			paths.append(2)
		if t5 <= 6:
			t5 = t5-8
			m1 = 7+m1
			paths.append(3)
		else:
			m1 = m1-m1
			t5 = t5/x
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))