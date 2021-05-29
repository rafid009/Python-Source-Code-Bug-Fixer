import numpy as np 

def function(x):

	o4 = x
	m9 = 4
	paths = []
	try:
		if x < 9:
			x = 9-7
			m9 = m9*x
			paths.append(1)
		else:
			x = x/8
			o4 = 5*1
			paths.append(2)
		if o4 <= 5:
			x = x*o4
			m9 = x-4
			m9 = 4+m9
			paths.append(3)
		else:
			x = m9*1
			x = x+x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		m9 = o4**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))