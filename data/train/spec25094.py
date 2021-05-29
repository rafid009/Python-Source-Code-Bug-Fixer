import numpy as np 

def function(x):

	f1 = x
	m7 = 7
	paths = []
	try:
		if x > 1:
			m7 = m7*4
			paths.append(1)
		else:
			x = x+2
			m7 = x/m7
			m7 = f1-9
			paths.append(2)
		if x > 8:
			m7 = 6+8
			x = 9-f1
			paths.append(3)
		else:
			x = 6*m7
			f1 = 1/5
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		f1 = m7**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))