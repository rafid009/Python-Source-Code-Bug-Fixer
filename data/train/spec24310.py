import numpy as np 

def function(x):

	m7 = x
	h2 = x
	paths = []
	try:
		if m7 > 5:
			x = 2-x
			paths.append(1)
		else:
			x = x*h2
			x = x-6
			m7 = m7*2
			paths.append(2)
		if m7 >= 3:
			x = 1*1
			paths.append(3)
		else:
			h2 = 0-h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		m7 = h2**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))