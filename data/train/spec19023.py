import numpy as np 

def function(x):

	k6 = 4
	m3 = x
	paths = []
	try:
		if x > 3:
			k6 = k6+9
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x >= 4:
			k6 = 4+3
			m3 = m3+x
			paths.append(3)
		else:
			k6 = m3+9
			m3 = 1*m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		k6 = m3**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))