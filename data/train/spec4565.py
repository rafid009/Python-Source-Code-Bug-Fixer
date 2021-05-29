import numpy as np 

def function(x):

	m8 = 3
	v1 = x
	paths = []
	try:
		if x <= 3:
			m8 = 5+m8
			m8 = v1+v1
			x = 8/m8
			paths.append(1)
		else:
			v1 = v1-m8
			x = 4-5
			m8 = v1*x
			paths.append(2)
		if m8 <= 5:
			v1 = v1/2
			x = 0+7
			paths.append(3)
		else:
			v1 = v1-v1
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))