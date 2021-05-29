import numpy as np 

def function(x):

	j0 = x
	m3 = 9
	paths = []
	try:
		if j0 > 7:
			m3 = m3-4
			x = 1-x
			j0 = j0-5
			paths.append(1)
		else:
			x = x/j0
			m3 = m3*j0
			m3 = 0+m3
			paths.append(2)
		if m3 < 6:
			j0 = 7*j0
			paths.append(3)
		else:
			m3 = 4/7
			j0 = j0+x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))