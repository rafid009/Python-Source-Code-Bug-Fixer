import numpy as np 

def function(x):

	m2 = 2
	v5 = 4
	paths = []
	try:
		if m2 < 2:
			m2 = m2+3
			m2 = 1-m2
			x = x/m2
			paths.append(1)
		else:
			v5 = v5/v5
			v5 = x+4
			v5 = v5+8
			paths.append(2)
		if m2 > 3:
			v5 = v5*m2
			m2 = m2/3
			paths.append(3)
		else:
			m2 = m2+3
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))