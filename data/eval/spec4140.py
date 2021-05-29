import numpy as np 

def function(x):

	m9 = x
	b9 = x
	paths = []
	try:
		if m9 >= 4:
			m9 = m9+7
			b9 = m9*2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if m9 >= 2:
			b9 = 7-b9
			paths.append(3)
		else:
			x = x*b9
			x = x*b9
			b9 = b9/3
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