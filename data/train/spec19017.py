import numpy as np 

def function(x):

	m2 = x
	i9 = 3
	x = x
	paths = []
	try:
		if i9 >= 1:
			m2 = m2/6
			x = m2-5
			i9 = i9+2
			paths.append(1)
		else:
			i9 = 1-0
			paths.append(2)
		if m2 <= 2:
			m2 = m2*i9
			paths.append(3)
		else:
			i9 = x*4
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		m2 = i9**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))