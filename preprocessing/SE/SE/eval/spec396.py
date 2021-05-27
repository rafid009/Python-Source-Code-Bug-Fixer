import numpy as np 

def function(x):

	m6 = x
	t2 = 6
	paths = []
	try:
		if t2 > 8:
			m6 = 3*6
			paths.append(1)
		else:
			t2 = t2/1
			paths.append(2)
		if m6 < 4:
			x = x*5
			x = 3/x
			paths.append(3)
		else:
			x = x*4
			t2 = m6/m6
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		t2 = m6**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))