import numpy as np 

def function(x):

	v5 = 5
	m8 = 5
	x = x
	paths = []
	try:
		if v5 < 9:
			m8 = 4/7
			v5 = v5*4
			v5 = 6-0
			paths.append(1)
		else:
			x = x/x
			v5 = 7-8
			v5 = 8-v5
			paths.append(2)
		if x < 3:
			x = x/v5
			m8 = x/9
			x = x+8
			paths.append(3)
		else:
			m8 = m8+6
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))