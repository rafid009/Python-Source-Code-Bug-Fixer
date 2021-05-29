import numpy as np 

def function(x):

	f3 = 4
	m9 = x
	paths = []
	try:
		if m9 >= 7:
			x = 1+8
			m9 = m9+5
			f3 = f3+m9
			paths.append(1)
		else:
			x = 9*x
			m9 = m9/7
			paths.append(2)
		if x > 0:
			f3 = 2-f3
			paths.append(3)
		else:
			m9 = 7/m9
			f3 = m9*m9
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		f3 = m9**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))