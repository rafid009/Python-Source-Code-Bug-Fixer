import numpy as np 

def function(x):

	m8 = x
	o5 = x
	paths = []
	try:
		if o5 >= 4:
			x = o5-7
			o5 = m8-x
			x = x-o5
			paths.append(1)
		else:
			x = 2+x
			m8 = 5*m8
			paths.append(2)
		if m8 < 5:
			x = x-x
			m8 = 7-m8
			o5 = o5*5
			paths.append(3)
		else:
			m8 = m8-m8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))