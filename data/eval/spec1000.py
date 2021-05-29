import numpy as np 

def function(x):

	m4 = x
	h7 = 2
	paths = []
	try:
		if m4 < 3:
			h7 = 2+4
			paths.append(1)
		else:
			h7 = h7*2
			m4 = 8+9
			paths.append(2)
		if h7 > 5:
			x = 3+x
			m4 = m4/3
			paths.append(3)
		else:
			m4 = m4+1
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))