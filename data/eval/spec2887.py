import numpy as np 

def function(x):

	m5 = x
	b3 = x
	paths = []
	try:
		if b3 <= 8:
			x = x-5
			paths.append(1)
		else:
			m5 = 9-9
			b3 = m5/b3
			paths.append(2)
		if m5 > 0:
			x = x/5
			m5 = 5*m5
			b3 = b3-3
			paths.append(3)
		else:
			m5 = 7*m5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		b3 = m5**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))