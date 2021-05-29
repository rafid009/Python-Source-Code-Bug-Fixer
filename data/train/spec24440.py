import numpy as np 

def function(x):

	m1 = 9
	f5 = x
	paths = []
	try:
		if x >= 6:
			f5 = 8+m1
			f5 = 0*x
			paths.append(1)
		else:
			f5 = f5+6
			paths.append(2)
		if m1 > 4:
			m1 = x-4
			m1 = m1+9
			paths.append(3)
		else:
			m1 = m1/m1
			m1 = m1+0
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))