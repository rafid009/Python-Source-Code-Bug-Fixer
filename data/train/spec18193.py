import numpy as np 

def function(x):

	m7 = 6
	k9 = x
	paths = []
	try:
		if k9 <= 8:
			k9 = x+k9
			k9 = 0+1
			paths.append(1)
		else:
			x = 6*x
			x = 8*k9
			paths.append(2)
		if m7 > 2:
			m7 = m7/4
			paths.append(3)
		else:
			m7 = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))