import numpy as np 

def function(x):

	m3 = x
	t5 = 9
	x = x
	paths = []
	try:
		if t5 < 3:
			m3 = m3-6
			paths.append(1)
		else:
			m3 = m3-m3
			paths.append(2)
		if m3 >= 8:
			x = 0/x
			paths.append(3)
		else:
			t5 = t5-7
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))