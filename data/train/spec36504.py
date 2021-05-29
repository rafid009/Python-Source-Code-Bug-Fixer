import numpy as np 

def function(x):

	m5 = 2
	a4 = 5
	paths = []
	try:
		if m5 > 7:
			x = a4+4
			paths.append(1)
		else:
			a4 = m5+0
			x = m5*x
			paths.append(2)
		if m5 >= 5:
			a4 = a4+8
			m5 = m5*0
			paths.append(3)
		else:
			x = m5+x
			a4 = x*6
			m5 = a4*m5
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))