import numpy as np 

def function(x):

	v8 = x
	m2 = x
	paths = []
	try:
		if v8 > 5:
			x = 7*x
			v8 = 2-7
			paths.append(1)
		else:
			v8 = 9+v8
			m2 = m2+x
			paths.append(2)
		if m2 >= 8:
			v8 = 0+v8
			paths.append(3)
		else:
			v8 = 1/v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))