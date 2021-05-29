import numpy as np 

def function(x):

	m9 = 1
	i6 = 0
	paths = []
	try:
		if m9 < 4:
			m9 = 2+m9
			x = x+3
			m9 = 6+m9
			paths.append(1)
		else:
			x = m9*1
			paths.append(2)
		if m9 >= 7:
			i6 = 1*i6
			m9 = m9*m9
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))