import numpy as np 

def function(x):

	m9 = x
	f9 = 8
	paths = []
	try:
		if m9 >= 7:
			m9 = m9*5
			paths.append(1)
		else:
			m9 = 0/m9
			x = 1-x
			f9 = 7-f9
			paths.append(2)
		if x >= 5:
			x = x/9
			x = 2*x
			paths.append(3)
		else:
			f9 = 3+0
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))