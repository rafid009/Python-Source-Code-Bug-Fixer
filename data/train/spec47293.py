import numpy as np 

def function(x):

	m7 = x
	i4 = 6
	paths = []
	try:
		if x <= 7:
			i4 = i4*1
			paths.append(1)
		else:
			m7 = 4-m7
			paths.append(2)
		if i4 < 1:
			m7 = 1*4
			m7 = 5-3
			m7 = i4*m7
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))