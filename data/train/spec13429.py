import numpy as np 

def function(x):

	m6 = 2
	t8 = x
	paths = []
	try:
		if t8 > 5:
			t8 = t8-4
			x = 5*x
			paths.append(1)
		else:
			t8 = t8+t8
			paths.append(2)
		if t8 >= 4:
			x = x-8
			x = x/1
			paths.append(3)
		else:
			t8 = m6/t8
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		m6 = t8**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))