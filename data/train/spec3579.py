import numpy as np 

def function(x):

	v7 = 9
	m8 = 0
	paths = []
	try:
		if x >= 0:
			m8 = m8*1
			paths.append(1)
		else:
			v7 = v7*5
			paths.append(2)
		if m8 <= 5:
			m8 = m8+x
			paths.append(3)
		else:
			m8 = m8/1
			v7 = v7+9
			m8 = m8/9
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