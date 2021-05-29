import numpy as np 

def function(x):

	m2 = x
	v4 = x
	paths = []
	try:
		if x < 3:
			m2 = m2/3
			paths.append(1)
		else:
			x = 9*x
			m2 = m2-7
			paths.append(2)
		if x < 6:
			v4 = v4-5
			v4 = v4-1
			m2 = 5/m2
			paths.append(3)
		else:
			x = x+5
			v4 = 0+x
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		v4 = m2**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))