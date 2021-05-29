import numpy as np 

def function(x):

	m7 = x
	b9 = x
	paths = []
	try:
		if m7 <= 8:
			x = x+1
			x = 4+7
			paths.append(1)
		else:
			x = 9*m7
			x = x+b9
			paths.append(2)
		if b9 <= 4:
			b9 = b9-7
			m7 = 0*2
			paths.append(3)
		else:
			x = m7+2
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		m7 = b9**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))