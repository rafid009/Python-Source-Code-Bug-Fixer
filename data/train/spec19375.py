import numpy as np 

def function(x):

	m2 = x
	f9 = 0
	paths = []
	try:
		if f9 > 2:
			f9 = m2/3
			x = x/6
			paths.append(1)
		else:
			x = x+f9
			paths.append(2)
		if f9 >= 5:
			m2 = f9-m2
			m2 = m2+8
			paths.append(3)
		else:
			f9 = m2+f9
			x = x*f9
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