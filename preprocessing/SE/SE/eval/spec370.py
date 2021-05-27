import numpy as np 

def function(x):

	m3 = x
	b1 = 8
	paths = []
	try:
		if b1 > 3:
			b1 = x/7
			m3 = 6+7
			x = x+1
			paths.append(1)
		else:
			m3 = 2+x
			b1 = 7*6
			paths.append(2)
		if m3 > 9:
			x = 7-x
			m3 = m3/m3
			paths.append(3)
		else:
			b1 = 2*b1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))