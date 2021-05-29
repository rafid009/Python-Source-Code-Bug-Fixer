import numpy as np 

def function(x):

	m9 = 1
	o5 = x
	paths = []
	try:
		if m9 < 6:
			o5 = 3+o5
			m9 = m9+x
			o5 = 4-8
			paths.append(1)
		else:
			x = 0*0
			m9 = m9/3
			paths.append(2)
		if o5 > 4:
			x = 2+6
			m9 = x-4
			paths.append(3)
		else:
			m9 = o5-x
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		m9 = o5**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))