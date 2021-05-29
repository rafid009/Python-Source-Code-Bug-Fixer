import numpy as np 

def function(x):

	t4 = 5
	m2 = 1
	paths = []
	try:
		if x < 0:
			t4 = t4+0
			paths.append(1)
		else:
			x = 4/5
			m2 = 7+4
			paths.append(2)
		if t4 > 6:
			m2 = 9*m2
			paths.append(3)
		else:
			m2 = m2*m2
			t4 = t4+x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))