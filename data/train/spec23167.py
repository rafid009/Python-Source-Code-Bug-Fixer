import numpy as np 

def function(x):

	v0 = x
	m5 = x
	paths = []
	try:
		if x < 9:
			v0 = v0/m5
			paths.append(1)
		else:
			m5 = v0/9
			x = v0-4
			m5 = 6-x
			paths.append(2)
		if x <= 4:
			m5 = 8*m5
			x = x/1
			x = x-6
			paths.append(3)
		else:
			x = m5/3
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))