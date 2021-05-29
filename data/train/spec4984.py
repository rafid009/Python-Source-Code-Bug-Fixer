import numpy as np 

def function(x):

	v6 = 8
	m3 = x
	paths = []
	try:
		if v6 < 6:
			v6 = v6*1
			v6 = v6+0
			m3 = 6-6
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if v6 > 0:
			m3 = m3+1
			paths.append(3)
		else:
			v6 = 8*1
			m3 = 9/m3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))