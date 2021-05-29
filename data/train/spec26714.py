import numpy as np 

def function(x):

	k7 = 9
	m7 = x
	paths = []
	try:
		if m7 < 8:
			k7 = k7-9
			k7 = m7*4
			paths.append(1)
		else:
			k7 = m7*2
			k7 = 7*k7
			paths.append(2)
		if m7 >= 0:
			x = 9*x
			paths.append(3)
		else:
			x = x/5
			x = 7*x
			m7 = m7+8
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))