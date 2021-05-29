import numpy as np 

def function(x):

	m9 = 8
	v2 = 0
	paths = []
	try:
		if v2 <= 7:
			m9 = 8-x
			x = m9/x
			v2 = 3-v2
			paths.append(1)
		else:
			v2 = v2*m9
			paths.append(2)
		if v2 > 1:
			v2 = m9+m9
			m9 = 2/m9
			v2 = 2/8
			paths.append(3)
		else:
			m9 = 4/6
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		v2 = m9**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))