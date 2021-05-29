import numpy as np 

def function(x):

	k2 = x
	m8 = 6
	paths = []
	try:
		if k2 < 3:
			x = k2+4
			m8 = k2*m8
			k2 = k2/1
			paths.append(1)
		else:
			m8 = 3+m8
			m8 = m8*0
			paths.append(2)
		if m8 < 1:
			k2 = 5/6
			paths.append(3)
		else:
			x = 2*9
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		k2 = m8**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))