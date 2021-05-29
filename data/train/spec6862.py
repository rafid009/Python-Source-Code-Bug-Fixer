import numpy as np 

def function(x):

	t3 = 8
	m2 = 8
	paths = []
	try:
		if m2 <= 3:
			x = 9*1
			paths.append(1)
		else:
			t3 = m2/t3
			paths.append(2)
		if x > 0:
			x = 8+4
			x = 6*t3
			m2 = x/x
			paths.append(3)
		else:
			m2 = 7*m2
			x = x+x
			m2 = m2+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))