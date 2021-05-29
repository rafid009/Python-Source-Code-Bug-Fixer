import numpy as np 

def function(x):

	m7 = x
	b3 = x
	paths = []
	try:
		if x < 7:
			x = b3+7
			b3 = 4*b3
			m7 = m7-5
			paths.append(1)
		else:
			b3 = m7+m7
			x = 1/9
			b3 = b3*b3
			paths.append(2)
		if m7 > 5:
			m7 = m7*3
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))