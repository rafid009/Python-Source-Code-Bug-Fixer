import numpy as np 

def function(x):

	m6 = x
	f2 = x
	paths = []
	try:
		if x < 2:
			f2 = 9-f2
			f2 = 7+m6
			f2 = m6+f2
			paths.append(1)
		else:
			m6 = 7-m6
			m6 = m6-f2
			x = x/2
			paths.append(2)
		if f2 >= 2:
			f2 = f2*f2
			m6 = 4-m6
			f2 = f2-7
			paths.append(3)
		else:
			x = x/7
			m6 = m6/6
			f2 = 8*f2
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		f2 = m6**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))