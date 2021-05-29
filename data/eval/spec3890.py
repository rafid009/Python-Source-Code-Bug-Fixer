import numpy as np 

def function(x):

	m0 = 8
	t3 = 4
	paths = []
	try:
		if m0 <= 8:
			m0 = x-m0
			paths.append(1)
		else:
			m0 = t3*m0
			x = t3-7
			paths.append(2)
		if t3 < 7:
			x = 2+5
			m0 = m0-x
			paths.append(3)
		else:
			t3 = m0-t3
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		t3 = m0**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))