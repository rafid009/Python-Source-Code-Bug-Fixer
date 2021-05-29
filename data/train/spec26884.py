import numpy as np 

def function(x):

	b3 = 1
	m8 = x
	paths = []
	try:
		if b3 > 4:
			x = 8-9
			paths.append(1)
		else:
			b3 = x+b3
			b3 = b3*3
			x = 7/x
			paths.append(2)
		if m8 <= 8:
			x = x-0
			paths.append(3)
		else:
			m8 = m8+x
			x = 1*0
			b3 = 0-b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		m8 = b3**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))