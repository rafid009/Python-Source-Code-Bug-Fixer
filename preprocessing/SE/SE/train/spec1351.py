import numpy as np 

def function(x):

	q8 = x
	m5 = 8
	paths = []
	try:
		if m5 > 1:
			q8 = q8+1
			paths.append(1)
		else:
			q8 = q8-x
			paths.append(2)
		if x <= 8:
			m5 = q8*m5
			x = 1+x
			paths.append(3)
		else:
			m5 = x/m5
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))