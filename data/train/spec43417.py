import numpy as np 

def function(x):

	m3 = 9
	a3 = 1
	paths = []
	try:
		if a3 <= 4:
			m3 = x*m3
			a3 = 4*0
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if x < 1:
			x = x+m3
			paths.append(3)
		else:
			m3 = 6+m3
			x = 5+x
			a3 = 9/m3
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