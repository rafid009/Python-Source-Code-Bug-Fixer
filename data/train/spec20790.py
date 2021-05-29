import numpy as np 

def function(x):

	j4 = x
	m7 = 3
	paths = []
	try:
		if j4 < 5:
			j4 = 7-j4
			j4 = 8*0
			paths.append(1)
		else:
			x = x*2
			m7 = x/4
			paths.append(2)
		if x <= 7:
			j4 = 5*j4
			x = x*8
			m7 = 0/m7
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))