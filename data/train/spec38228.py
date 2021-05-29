import numpy as np 

def function(x):

	m1 = 8
	v8 = x
	paths = []
	try:
		if v8 >= 2:
			v8 = m1*6
			x = x-7
			m1 = v8/2
			paths.append(1)
		else:
			v8 = v8+m1
			x = 9+x
			paths.append(2)
		if v8 > 6:
			v8 = v8+v8
			paths.append(3)
		else:
			m1 = 7-v8
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