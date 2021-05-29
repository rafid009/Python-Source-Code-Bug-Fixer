import numpy as np 

def function(x):

	m3 = x
	v9 = x
	paths = []
	try:
		if v9 >= 1:
			v9 = 2-v9
			v9 = 1-m3
			paths.append(1)
		else:
			v9 = v9*7
			m3 = m3-5
			paths.append(2)
		if x > 0:
			v9 = x/v9
			m3 = m3+m3
			paths.append(3)
		else:
			m3 = 1-m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		v9 = m3**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))