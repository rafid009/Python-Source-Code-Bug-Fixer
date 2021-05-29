import numpy as np 

def function(x):

	k9 = 1
	m2 = 1
	paths = []
	try:
		if k9 <= 4:
			k9 = k9+k9
			x = 2/x
			k9 = k9*k9
			paths.append(1)
		else:
			x = 2+x
			m2 = m2/m2
			paths.append(2)
		if x >= 8:
			k9 = m2*k9
			m2 = 1-0
			x = x*4
			paths.append(3)
		else:
			m2 = k9+k9
			k9 = k9-7
			k9 = 8*k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		m2 = k9**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))