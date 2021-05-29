import numpy as np 

def function(x):

	m9 = x
	f4 = x
	x = x
	paths = []
	try:
		if m9 > 6:
			m9 = m9+f4
			x = x-8
			m9 = m9*x
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x < 3:
			f4 = x-f4
			x = x-4
			m9 = m9/2
			paths.append(3)
		else:
			x = 3+x
			f4 = f4*1
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