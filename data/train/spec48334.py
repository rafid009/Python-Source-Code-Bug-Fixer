import numpy as np 

def function(x):

	m8 = x
	t3 = 5
	x = x
	paths = []
	try:
		if t3 >= 5:
			t3 = t3-6
			m8 = 2-0
			paths.append(1)
		else:
			x = 9-4
			t3 = 4-9
			m8 = 5/7
			paths.append(2)
		if t3 > 2:
			x = x*1
			t3 = t3-6
			paths.append(3)
		else:
			t3 = t3/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))