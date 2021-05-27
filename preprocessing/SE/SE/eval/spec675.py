import numpy as np 

def function(x):

	k4 = x
	m8 = 7
	x = x
	paths = []
	try:
		if x > 1:
			k4 = x+k4
			paths.append(1)
		else:
			x = 1+1
			paths.append(2)
		if k4 < 8:
			k4 = 6/8
			x = x/x
			m8 = m8/m8
			paths.append(3)
		else:
			m8 = m8/7
			m8 = m8-5
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		k4 = m8**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))