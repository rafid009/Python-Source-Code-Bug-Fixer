import numpy as np 

def function(x):

	f4 = 3
	m7 = x
	paths = []
	try:
		if m7 >= 9:
			x = 4/f4
			paths.append(1)
		else:
			x = f4*1
			paths.append(2)
		if x < 1:
			m7 = 4/m7
			paths.append(3)
		else:
			f4 = 1*f4
			x = 1+f4
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))