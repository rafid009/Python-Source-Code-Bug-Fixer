import numpy as np 

def function(x):

	m8 = x
	t2 = 2
	paths = []
	try:
		if x >= 1:
			x = t2+x
			t2 = 7/8
			paths.append(1)
		else:
			m8 = 1/m8
			paths.append(2)
		if t2 < 2:
			x = 0-2
			t2 = t2*1
			paths.append(3)
		else:
			m8 = m8+x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))