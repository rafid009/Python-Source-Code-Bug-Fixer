import numpy as np 

def function(x):

	m7 = x
	i2 = x
	x = 2
	paths = []
	try:
		if m7 > 8:
			i2 = i2-x
			m7 = 8-1
			x = 9-0
			paths.append(1)
		else:
			i2 = 6*i2
			x = m7*x
			paths.append(2)
		if m7 <= 6:
			m7 = m7+5
			i2 = i2+6
			paths.append(3)
		else:
			i2 = i2/4
			x = x-7
			m7 = i2+m7
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		m7 = i2**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))