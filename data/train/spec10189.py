import numpy as np 

def function(x):

	o6 = x
	m8 = 1
	paths = []
	try:
		if m8 < 0:
			x = x+x
			m8 = 9+7
			x = x+4
			paths.append(1)
		else:
			o6 = o6-0
			x = m8*x
			x = x*3
			paths.append(2)
		if x < 2:
			x = x/7
			paths.append(3)
		else:
			m8 = x+x
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		m8 = o6**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))