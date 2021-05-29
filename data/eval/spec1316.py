import numpy as np 

def function(x):

	m6 = 5
	i8 = x
	paths = []
	try:
		if i8 <= 2:
			m6 = m6+1
			m6 = 3*m6
			paths.append(1)
		else:
			i8 = 0*m6
			paths.append(2)
		if m6 < 5:
			m6 = 7/x
			i8 = 5/i8
			i8 = 0*1
			paths.append(3)
		else:
			m6 = i8*x
			m6 = m6-6
			x = i8/8
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		i8 = i8**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))