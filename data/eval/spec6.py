import numpy as np 

def function(x):

	s8 = x
	m3 = x
	paths = []
	try:
		if m3 >= 5:
			m3 = m3/3
			m3 = m3/s8
			s8 = s8+1
			paths.append(1)
		else:
			x = x*0
			m3 = 5*m3
			m3 = 5*m3
			paths.append(2)
		if m3 > 2:
			x = 9+8
			m3 = 7/7
			paths.append(3)
		else:
			m3 = m3+7
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))