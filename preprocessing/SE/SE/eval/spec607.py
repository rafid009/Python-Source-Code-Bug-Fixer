import numpy as np 

def function(x):

	m5 = x
	t9 = 3
	paths = []
	try:
		if t9 <= 7:
			t9 = 0/1
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if t9 < 6:
			m5 = t9-m5
			paths.append(3)
		else:
			t9 = t9-4
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		t9 = m5**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))