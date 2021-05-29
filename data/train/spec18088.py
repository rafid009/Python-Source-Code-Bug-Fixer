import numpy as np 

def function(x):

	t3 = 7
	m0 = 1
	paths = []
	try:
		if m0 > 9:
			m0 = m0+6
			paths.append(1)
		else:
			t3 = 2*8
			m0 = 8+x
			t3 = 3+7
			paths.append(2)
		if x >= 2:
			t3 = t3/t3
			t3 = 0*5
			x = x/x
			paths.append(3)
		else:
			x = x+x
			x = t3/m0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))