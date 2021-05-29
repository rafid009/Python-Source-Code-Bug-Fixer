import numpy as np 

def function(x):

	m0 = 4
	t9 = x
	paths = []
	try:
		if m0 <= 8:
			t9 = 5/t9
			paths.append(1)
		else:
			x = 4+0
			paths.append(2)
		if m0 > 9:
			m0 = 3*m0
			x = x-6
			x = m0/6
			paths.append(3)
		else:
			m0 = 0-7
			m0 = m0-x
			x = 8+t9
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		t9 = m0**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))