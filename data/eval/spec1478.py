import numpy as np 

def function(x):

	m5 = 1
	m9 = 3
	paths = []
	try:
		if x > 0:
			x = x*x
			m5 = m5*8
			m5 = m5+2
			paths.append(1)
		else:
			m9 = m9-0
			paths.append(2)
		if m9 <= 4:
			m9 = m9-7
			paths.append(3)
		else:
			x = m9-5
			m5 = m9-3
			x = x-8
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))