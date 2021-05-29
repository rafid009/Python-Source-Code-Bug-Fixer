import numpy as np 

def function(x):

	f6 = x
	m8 = x
	paths = []
	try:
		if m8 > 2:
			x = 3-x
			m8 = 1-m8
			paths.append(1)
		else:
			f6 = 4+f6
			m8 = 7*0
			paths.append(2)
		if x > 4:
			x = x+1
			m8 = m8/x
			paths.append(3)
		else:
			m8 = m8/6
			f6 = 5-f6
			x = f6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))