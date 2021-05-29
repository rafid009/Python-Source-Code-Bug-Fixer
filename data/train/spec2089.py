import numpy as np 

def function(x):

	n2 = 7
	m9 = x
	paths = []
	try:
		if x < 7:
			x = x/n2
			n2 = m9+n2
			x = x*m9
			paths.append(1)
		else:
			n2 = n2+9
			x = 2/1
			paths.append(2)
		if m9 > 5:
			m9 = m9-9
			x = x-3
			paths.append(3)
		else:
			m9 = 6-m9
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))