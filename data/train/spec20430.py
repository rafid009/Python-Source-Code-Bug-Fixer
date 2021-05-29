import numpy as np 

def function(x):

	m3 = x
	t9 = x
	paths = []
	try:
		if t9 <= 2:
			x = 9-x
			t9 = t9*t9
			t9 = m3-t9
			paths.append(1)
		else:
			m3 = m3*t9
			x = 0/5
			paths.append(2)
		if x >= 1:
			x = 0*m3
			x = t9-x
			t9 = t9-2
			paths.append(3)
		else:
			m3 = t9-m3
			m3 = m3+0
			t9 = 7*8
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		t9 = m3**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))