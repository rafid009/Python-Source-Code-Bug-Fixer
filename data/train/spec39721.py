import numpy as np 

def function(x):

	y1 = x
	m0 = 1
	paths = []
	try:
		if y1 <= 5:
			x = x/1
			m0 = y1/m0
			x = 0+x
			paths.append(1)
		else:
			y1 = 6-y1
			y1 = y1*y1
			m0 = 9/x
			paths.append(2)
		if m0 < 4:
			m0 = m0*8
			x = x*0
			m0 = 7+y1
			paths.append(3)
		else:
			x = 9+2
			y1 = 9-8
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))