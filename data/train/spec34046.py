import numpy as np 

def function(x):

	v5 = 2
	m3 = x
	paths = []
	try:
		if x > 9:
			x = x*0
			paths.append(1)
		else:
			m3 = m3-5
			x = 4+8
			paths.append(2)
		if v5 <= 2:
			x = 1*v5
			paths.append(3)
		else:
			m3 = m3-6
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))