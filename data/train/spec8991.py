import numpy as np 

def function(x):

	t7 = 9
	m4 = x
	paths = []
	try:
		if m4 < 9:
			m4 = m4/9
			paths.append(1)
		else:
			t7 = 8/t7
			x = m4+2
			paths.append(2)
		if x >= 3:
			x = 6-9
			m4 = 2+t7
			m4 = m4-8
			paths.append(3)
		else:
			t7 = 9*4
			m4 = 5/m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		t7 = m4**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))