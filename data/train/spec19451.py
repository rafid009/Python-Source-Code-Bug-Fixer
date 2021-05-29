import numpy as np 

def function(x):

	f8 = x
	m7 = x
	paths = []
	try:
		if m7 < 3:
			m7 = x+m7
			m7 = m7-4
			x = 5+m7
			paths.append(1)
		else:
			m7 = 5/6
			f8 = x/x
			paths.append(2)
		if f8 >= 9:
			m7 = f8*m7
			x = m7*x
			paths.append(3)
		else:
			m7 = x+7
			x = 3*x
			f8 = f8*1
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		f8 = m7**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))