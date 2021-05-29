import numpy as np 

def function(x):

	m9 = x
	f2 = 2
	paths = []
	try:
		if x >= 1:
			f2 = f2-2
			m9 = m9+1
			m9 = 5/7
			paths.append(1)
		else:
			m9 = m9*5
			paths.append(2)
		if f2 >= 1:
			x = x-5
			x = 0-f2
			paths.append(3)
		else:
			x = f2/1
			f2 = f2-6
			f2 = x+f2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))