import numpy as np 

def function(x):

	o5 = x
	m0 = x
	paths = []
	try:
		if o5 >= 6:
			o5 = 6*o5
			paths.append(1)
		else:
			m0 = o5-0
			m0 = 4/o5
			x = m0/8
			paths.append(2)
		if m0 >= 1:
			x = 5/9
			o5 = 7/o5
			o5 = o5*1
			paths.append(3)
		else:
			o5 = o5-4
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))