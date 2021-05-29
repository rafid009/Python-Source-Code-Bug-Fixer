import numpy as np 

def function(x):

	m6 = 6
	t9 = x
	paths = []
	try:
		if t9 <= 8:
			t9 = t9+t9
			m6 = 5+4
			paths.append(1)
		else:
			t9 = x/m6
			t9 = 9+t9
			t9 = 1-1
			paths.append(2)
		if t9 >= 3:
			m6 = m6-t9
			paths.append(3)
		else:
			m6 = m6/6
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))