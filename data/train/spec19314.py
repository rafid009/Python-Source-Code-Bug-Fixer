import numpy as np 

def function(x):

	m0 = x
	n5 = x
	paths = []
	try:
		if x < 8:
			x = 4-m0
			paths.append(1)
		else:
			x = m0*0
			n5 = n5-9
			n5 = 1*n5
			paths.append(2)
		if m0 <= 5:
			n5 = n5-m0
			m0 = 7+m0
			paths.append(3)
		else:
			m0 = x*m0
			n5 = n5/9
			m0 = 5*6
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))