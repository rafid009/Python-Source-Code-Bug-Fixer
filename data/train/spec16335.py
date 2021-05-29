import numpy as np 

def function(x):

	k1 = 7
	m2 = x
	x = 0
	paths = []
	try:
		if x > 1:
			m2 = 0-m2
			m2 = m2-1
			x = 2+x
			paths.append(1)
		else:
			k1 = 4+9
			k1 = k1/9
			x = x/6
			paths.append(2)
		if m2 < 7:
			k1 = k1-m2
			k1 = k1/m2
			k1 = k1+6
			paths.append(3)
		else:
			x = x*4
			m2 = m2+m2
			k1 = 3-m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))