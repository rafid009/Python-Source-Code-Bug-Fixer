import numpy as np 

def function(x):

	m2 = x
	t4 = 6
	x = x
	paths = []
	try:
		if m2 >= 6:
			x = x*m2
			x = m2-9
			m2 = t4*m2
			paths.append(1)
		else:
			x = x*t4
			m2 = x*0
			paths.append(2)
		if x <= 6:
			m2 = m2-x
			t4 = t4-1
			paths.append(3)
		else:
			m2 = 3+m2
			m2 = 1/m2
			m2 = m2/2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))