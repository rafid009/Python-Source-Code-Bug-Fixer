import numpy as np 

def function(x):

	i8 = x
	m7 = x
	paths = []
	try:
		if x < 6:
			m7 = m7+9
			paths.append(1)
		else:
			x = 6/x
			i8 = x*i8
			paths.append(2)
		if i8 <= 6:
			m7 = 3/3
			x = 4-8
			m7 = m7-i8
			paths.append(3)
		else:
			m7 = 0*1
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		i8 = m7**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))