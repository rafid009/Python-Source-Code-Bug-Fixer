import numpy as np 

def function(x):

	k6 = x
	m3 = x
	paths = []
	try:
		if x < 6:
			m3 = x+m3
			x = 5*m3
			k6 = k6-m3
			paths.append(1)
		else:
			m3 = 4+m3
			k6 = k6*3
			paths.append(2)
		if m3 >= 6:
			k6 = 3+m3
			k6 = 2*k6
			k6 = k6+8
			paths.append(3)
		else:
			m3 = 9*m3
			m3 = 1/m3
			m3 = x-m3
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))