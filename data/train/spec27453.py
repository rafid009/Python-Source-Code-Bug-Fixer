import numpy as np 

def function(x):

	m8 = x
	j6 = 4
	paths = []
	try:
		if m8 < 8:
			m8 = m8+x
			j6 = 0-5
			paths.append(1)
		else:
			m8 = 8-x
			paths.append(2)
		if j6 > 2:
			j6 = 4+m8
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))