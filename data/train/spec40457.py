import numpy as np 

def function(x):

	m2 = x
	k9 = 5
	paths = []
	try:
		if m2 < 7:
			m2 = m2/3
			k9 = 3*k9
			paths.append(1)
		else:
			m2 = 3+m2
			m2 = m2/3
			paths.append(2)
		if m2 <= 4:
			m2 = m2/6
			paths.append(3)
		else:
			m2 = m2+9
			x = 4-x
			k9 = k9+6
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		k9 = m2**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))