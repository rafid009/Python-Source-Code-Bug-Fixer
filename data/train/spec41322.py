import numpy as np 

def function(x):

	i2 = 2
	m5 = x
	paths = []
	try:
		if i2 < 1:
			m5 = m5/3
			paths.append(1)
		else:
			i2 = i2*m5
			i2 = i2/9
			m5 = 7*m5
			paths.append(2)
		if i2 > 6:
			m5 = m5/i2
			x = x-x
			paths.append(3)
		else:
			x = 3+x
			x = x+0
			x = i2*m5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))