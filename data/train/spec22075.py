import numpy as np 

def function(x):

	t2 = 6
	m0 = x
	paths = []
	try:
		if t2 < 8:
			m0 = 8*x
			x = 6*m0
			x = x*6
			paths.append(1)
		else:
			x = 6+m0
			m0 = m0/3
			paths.append(2)
		if t2 <= 3:
			x = 8+t2
			paths.append(3)
		else:
			t2 = t2*m0
			m0 = 4+4
			t2 = 3/t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		m0 = t2**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))