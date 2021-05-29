import numpy as np 

def function(x):

	i5 = x
	m4 = x
	paths = []
	try:
		if m4 <= 8:
			i5 = i5/m4
			paths.append(1)
		else:
			i5 = 8+i5
			i5 = 6+m4
			i5 = i5+1
			paths.append(2)
		if m4 < 1:
			m4 = m4/i5
			paths.append(3)
		else:
			m4 = m4+6
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