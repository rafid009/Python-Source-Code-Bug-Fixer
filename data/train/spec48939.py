import numpy as np 

def function(x):

	k2 = x
	m3 = x
	paths = []
	try:
		if x < 6:
			m3 = 3+m3
			paths.append(1)
		else:
			m3 = 8*m3
			k2 = k2+3
			paths.append(2)
		if m3 <= 3:
			m3 = m3+3
			x = x+3
			m3 = 2-5
			paths.append(3)
		else:
			k2 = 2-k2
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))