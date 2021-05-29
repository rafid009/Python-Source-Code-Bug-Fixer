import numpy as np 

def function(x):

	v8 = 4
	m0 = x
	paths = []
	try:
		if m0 < 7:
			v8 = x+v8
			v8 = 6-m0
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if x < 1:
			m0 = m0+x
			paths.append(3)
		else:
			x = x/v8
			x = x/x
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