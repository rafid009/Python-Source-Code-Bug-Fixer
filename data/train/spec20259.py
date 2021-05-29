import numpy as np 

def function(x):

	m6 = 7
	f8 = x
	paths = []
	try:
		if f8 > 6:
			m6 = 6+m6
			m6 = 4+0
			paths.append(1)
		else:
			m6 = 2-5
			m6 = 8+4
			m6 = m6+1
			paths.append(2)
		if f8 > 7:
			f8 = f8-x
			x = x*9
			m6 = f8-9
			paths.append(3)
		else:
			f8 = 1-2
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		f8 = m6**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))