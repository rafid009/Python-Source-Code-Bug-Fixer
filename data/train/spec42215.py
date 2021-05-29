import numpy as np 

def function(x):

	m8 = x
	i1 = 7
	paths = []
	try:
		if i1 <= 0:
			x = 9-m8
			x = 4*4
			paths.append(1)
		else:
			i1 = i1*m8
			i1 = 6/7
			i1 = i1/4
			paths.append(2)
		if m8 > 7:
			x = 4+x
			x = 8*3
			m8 = m8*x
			paths.append(3)
		else:
			x = x/m8
			m8 = x*m8
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		i1 = m8**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))