import numpy as np 

def function(x):

	m6 = x
	o6 = 7
	paths = []
	try:
		if o6 < 3:
			m6 = 9-m6
			x = m6/8
			x = x/6
			paths.append(1)
		else:
			x = x/x
			o6 = 4-o6
			m6 = m6/x
			paths.append(2)
		if m6 <= 5:
			o6 = 2-m6
			paths.append(3)
		else:
			o6 = 3/o6
			x = m6*9
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))