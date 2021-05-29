import numpy as np 

def function(x):

	v8 = x
	m6 = x
	paths = []
	try:
		if x < 7:
			m6 = m6*x
			paths.append(1)
		else:
			x = 5+v8
			m6 = m6/x
			paths.append(2)
		if x <= 0:
			m6 = m6/m6
			paths.append(3)
		else:
			v8 = v8+8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))