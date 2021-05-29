import numpy as np 

def function(x):

	a0 = x
	m8 = 1
	paths = []
	try:
		if x <= 5:
			m8 = a0+x
			paths.append(1)
		else:
			a0 = a0*1
			m8 = m8/m8
			paths.append(2)
		if m8 < 3:
			a0 = 1+a0
			paths.append(3)
		else:
			a0 = m8*x
			x = x/6
			a0 = a0*1
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		a0 = m8**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))