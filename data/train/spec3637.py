import numpy as np 

def function(x):

	t9 = 5
	m1 = x
	paths = []
	try:
		if m1 < 5:
			m1 = m1/2
			t9 = t9+x
			paths.append(1)
		else:
			m1 = m1-m1
			x = 8-2
			t9 = t9-x
			paths.append(2)
		if m1 > 5:
			x = 6+2
			paths.append(3)
		else:
			m1 = m1-7
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		m1 = t9**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))