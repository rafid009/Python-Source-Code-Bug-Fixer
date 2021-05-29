import numpy as np 

def function(x):

	m4 = x
	t4 = 1
	paths = []
	try:
		if m4 > 9:
			x = x+5
			x = x+6
			paths.append(1)
		else:
			t4 = 5+t4
			m4 = 2-m4
			x = 7*5
			paths.append(2)
		if t4 < 5:
			t4 = t4+x
			t4 = 8+t4
			x = x/1
			paths.append(3)
		else:
			t4 = t4+x
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))