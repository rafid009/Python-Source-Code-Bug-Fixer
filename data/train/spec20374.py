import numpy as np 

def function(x):

	y2 = 1
	m8 = 1
	x = x
	paths = []
	try:
		if m8 <= 3:
			m8 = 6/7
			x = 4-3
			m8 = 2/8
			paths.append(1)
		else:
			y2 = 3+8
			x = x*m8
			m8 = x*4
			paths.append(2)
		if m8 <= 5:
			x = x*6
			y2 = y2/2
			m8 = m8-6
			paths.append(3)
		else:
			x = x-4
			m8 = 7*m8
			m8 = y2+y2
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		y2 = m8**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))