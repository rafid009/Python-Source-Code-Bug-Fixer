import numpy as np 

def function(x):

	m8 = x
	a6 = 2
	paths = []
	try:
		if x >= 8:
			a6 = a6*8
			a6 = 6+5
			x = 2*x
			paths.append(1)
		else:
			a6 = m8/m8
			a6 = a6*6
			m8 = 0+a6
			paths.append(2)
		if x < 5:
			a6 = a6/4
			a6 = x*3
			paths.append(3)
		else:
			x = x/6
			x = x*a6
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		m8 = a6**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))