import numpy as np 

def function(x):

	t2 = 6
	m5 = x
	paths = []
	try:
		if x < 4:
			x = x/1
			paths.append(1)
		else:
			x = t2/1
			m5 = 0*x
			paths.append(2)
		if m5 >= 5:
			m5 = m5/t2
			m5 = 4*t2
			x = x/8
			paths.append(3)
		else:
			x = x-9
			t2 = 7/4
			t2 = m5+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))