import numpy as np 

def function(x):

	j2 = x
	m8 = x
	paths = []
	try:
		if j2 < 5:
			m8 = m8*4
			paths.append(1)
		else:
			m8 = m8*9
			j2 = j2-6
			m8 = x+m8
			paths.append(2)
		if j2 >= 8:
			m8 = m8*x
			x = 1/5
			paths.append(3)
		else:
			x = j2-x
			x = m8-7
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))