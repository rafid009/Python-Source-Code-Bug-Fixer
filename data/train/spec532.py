import numpy as np 

def function(x):

	v1 = x
	m7 = x
	paths = []
	try:
		if v1 >= 8:
			m7 = 9*v1
			paths.append(1)
		else:
			v1 = 4-9
			m7 = 8*v1
			m7 = v1*m7
			paths.append(2)
		if m7 < 4:
			m7 = m7*m7
			paths.append(3)
		else:
			m7 = 2+7
			x = v1*x
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))