import numpy as np 

def function(x):

	d4 = 2
	m7 = x
	x = x
	paths = []
	try:
		if m7 >= 9:
			x = 1-d4
			m7 = 1+m7
			paths.append(1)
		else:
			d4 = d4*0
			x = x/3
			d4 = d4-m7
			paths.append(2)
		if x <= 0:
			d4 = 1-5
			d4 = d4/3
			paths.append(3)
		else:
			m7 = m7*4
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))