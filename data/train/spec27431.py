import numpy as np 

def function(x):

	m9 = x
	k7 = 9
	paths = []
	try:
		if m9 >= 4:
			x = x/x
			m9 = k7*k7
			m9 = m9+k7
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x < 4:
			x = x/4
			paths.append(3)
		else:
			m9 = m9+5
			x = k7/k7
			k7 = k7*x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		k7 = m9**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))