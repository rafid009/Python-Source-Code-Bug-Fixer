import numpy as np 

def function(x):

	b3 = x
	m3 = 7
	paths = []
	try:
		if m3 >= 2:
			x = 5/x
			b3 = b3/8
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if m3 <= 7:
			m3 = m3/8
			x = m3*0
			paths.append(3)
		else:
			m3 = 5*3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))