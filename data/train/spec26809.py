import numpy as np 

def function(x):

	m4 = x
	v5 = x
	paths = []
	try:
		if v5 > 4:
			v5 = 1*x
			paths.append(1)
		else:
			m4 = 9+m4
			v5 = x/v5
			x = x+2
			paths.append(2)
		if x >= 4:
			v5 = 8*5
			x = x-3
			paths.append(3)
		else:
			v5 = v5-8
			v5 = 1*v5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		m4 = v5**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))