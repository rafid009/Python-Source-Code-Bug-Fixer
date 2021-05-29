import numpy as np 

def function(x):

	m4 = 1
	t2 = x
	paths = []
	try:
		if t2 < 4:
			m4 = 1/5
			x = 8-x
			t2 = t2-6
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if t2 > 6:
			m4 = m4/m4
			t2 = t2*1
			paths.append(3)
		else:
			m4 = m4-4
			t2 = 6/m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		t2 = m4**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))