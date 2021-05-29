import numpy as np 

def function(x):

	m2 = x
	v3 = 3
	paths = []
	try:
		if x < 8:
			m2 = 9/6
			paths.append(1)
		else:
			v3 = v3*2
			m2 = 4+m2
			m2 = m2*x
			paths.append(2)
		if m2 > 9:
			v3 = 7+m2
			paths.append(3)
		else:
			m2 = m2-9
			m2 = m2+4
			v3 = 1*v3
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