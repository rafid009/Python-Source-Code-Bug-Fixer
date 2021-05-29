import numpy as np 

def function(x):

	m0 = 5
	d1 = x
	x = 4
	paths = []
	try:
		if d1 > 3:
			x = x/m0
			paths.append(1)
		else:
			d1 = d1*x
			m0 = 9-4
			paths.append(2)
		if m0 <= 8:
			d1 = d1*m0
			paths.append(3)
		else:
			x = 6+3
			m0 = m0*0
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))