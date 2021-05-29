import numpy as np 

def function(x):

	y4 = x
	m7 = 9
	x = 4
	paths = []
	try:
		if m7 <= 8:
			y4 = 5/9
			y4 = 9/7
			paths.append(1)
		else:
			m7 = 4-x
			m7 = x/8
			m7 = 8*m7
			paths.append(2)
		if y4 > 7:
			y4 = x-7
			paths.append(3)
		else:
			m7 = x/m7
			y4 = y4/y4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		m7 = y4**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))