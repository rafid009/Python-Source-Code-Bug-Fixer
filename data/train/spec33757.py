import numpy as np 

def function(x):

	j3 = x
	m8 = 1
	paths = []
	try:
		if x < 8:
			j3 = j3-2
			m8 = m8+4
			paths.append(1)
		else:
			j3 = 8/j3
			paths.append(2)
		if j3 <= 6:
			m8 = m8+j3
			paths.append(3)
		else:
			m8 = m8*9
			j3 = j3-0
			m8 = m8+x
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))