import numpy as np 

def function(x):

	m7 = 5
	i9 = 0
	paths = []
	try:
		if x >= 2:
			x = x-i9
			paths.append(1)
		else:
			m7 = 9-m7
			i9 = 1-4
			m7 = m7*2
			paths.append(2)
		if x <= 0:
			m7 = m7/4
			x = x*2
			paths.append(3)
		else:
			i9 = 7+i9
			i9 = 7*i9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		m7 = i9**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))